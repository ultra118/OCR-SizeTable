## YOLO-v2 trasfer-learning in jupyter

- 반드시 같은 경로에 `darkflow`를 설치해줘야함

```bash
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
python setup.py build_ext --inplace
pip install .
```

- issue 생기면 이전 readme 참조
- `labels.txt`는 분류될 class label로 지정해줘야함
  - `table`
- `.cfg` 설정
  - classes 수정해주고
  - filters 수정 (classes + 5) * 5로
- `bin`폴더 만들고 `yolo.weight`넣어줌
- `ckpt`폴더도 만들어놔야 나중에 트레이닝한 체크포인트 저장됨

