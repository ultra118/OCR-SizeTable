import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# 열을 잘라주는 함수
def crop_col_img(img_path):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x_len = img_gray.shape[1]
    y_len = img_gray.shape[0]

    threshold = int(y_len / 200 * 0.6)

    check_list = []
    for x in range(x_len):
        not_white = 0
        for y in range(0, y_len, 200):
            if img_gray[y][x] != 255:
                not_white += 1
        # 임계치보다 white가 아닌부분이 많이 나오면 check_list에 추가해줌
        if not_white > threshold:
            check_list.append(x)
    if len(check_list) > 0:
        # check list에서 가장 작은 x좌표, 가장 큰 x좌표로 indexing
        x_min_point = np.min(check_list)
        x_max_point = np.max(check_list)
        crop_img = img[:, x_min_point:x_max_point]
        if crop_img.shape[1] == 0:
            return img
        return crop_img
    # check list를 하나도 못찾으면 그냥 이미지 리턴
    return img


# 이미지를 행을 분리시켜주는 함수
def split_img(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    y_shape = img_gray.shape[0]
    x_shape = img_gray.shape[1]
    split_point_y = []
    line = 0
    for y in range(y_shape):
        ck_color = 0
        for x in range(0, x_shape, 15):
            # 한줄이 다 같은색이면
            if img_gray[y][x] == img_gray[y][0]:
                ck_color += 1
            else:
                line = 0
                break
        if ck_color >= int(x_shape/15):
            line += 1
            if line == 25:
                split_point_y.append(y)
                line = 0
    split_img_list = []
    # 분리 못하면 그냥 원래 img 리턴
    if len(split_point_y) == 0:
        return [img]
    start = 0
    for point in split_point_y:
        if (point - start) > 100:
            split_img_list.append(img[start:point][:])
        start = point
    if (point - start) > 100:
        split_img_list.append(img[start:][:])
#     print('len(split_point_y) : {} '.format(len(split_point_y)))
#     print('len(split_img_list) : {} '.format(len(split_img_list)))

    return split_img_list


# 이미지를 이어붙여주는 함수
def img_concat(split_img_list):
    sum_len = 0
    concat_img_list = []
    over_1500_img = []
    for img in split_img_list:
        concat_img_list.append(img)
        sum_len = sum_len + img.shape[0]
        # 1500보다 길면 지금까지의 append된 이미지를 concat
        if sum_len > 1500:
            over_1500_img.append(np.concatenate(concat_img_list, axis=0))
            concat_img_list = []
            sum_len = 0
        else:
            continue
    # 딱 1500별로 잘리는 케이스 아니면 나머지에 더해줌
    if len(concat_img_list) != 0:
        over_1500_img.append(np.concatenate(concat_img_list, axis=0))
    return over_1500_img


# working_path 돌면서 모든 이미지 처리한 후 saving_path에 저장
def image_preprocessing(working_path, saving_path):
    img_list = os.listdir(working_path)
    for i, img in enumerate(img_list):
        if i % 50 == 0:
            print(f'{i}/{len(img_list)} split...')
        if '.png' in img or 'jpg' in img:
            img_name = img.split('.')[0]
            img_path = os.path.join(working_path, img)

            # print(f'img_name : {img_name}, img_path  : {img_path}')
            # 양쪽 여백 잘라주고
            crop_img = crop_col_img(img_path)
            # 이미지 분리
            split_img_list = split_img(crop_img)
            # 적당히 붙여주기
            concat_img_list = img_concat(split_img_list)
            for idx, concat_img in enumerate(concat_img_list):
                concat_img_name = f'{img_name}_{idx}.jpg'
                # if concat_img.shape[0] > 10000:
                #     print(f'{concat_img_name}은 분리가 안됨')
                #     continue
                cv2.imwrite(os.path.join(saving_path, concat_img_name), concat_img)