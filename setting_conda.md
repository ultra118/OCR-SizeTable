# Setting tensorflow-gpu

- version에 맞는 CUDA설치

  - [CUDA 10.0](<https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal>)
    - 빠른설치로 설치할떄 visual studio 에러가나면 visual studio community를 다운
      - visual studio community워크로드의 C++부분 check하고 다운로드
    - 그리고 사용자 설치로 visual studio부분 uncheck하고 다운로드해보도록 함

- version에 맞는 cuDNN 설치

  - [cuDNN](<https://developer.nvidia.com/rdp/cudnn-download>)

    - NVIDIA 로그인 필요

  - cuDNN 압출 풀고 해당 파일들을 모두 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0`경로에 덮어쓰기

    ![image](https://user-images.githubusercontent.com/28910538/58747956-1c44f280-84ad-11e9-827a-445f2a97e73e.png)

- conda envs 설정

  - 가상환경 만들기

  ```bash
  conda create -n ocr_env python=3.6
  ```

  - 가상환경 리스트 확인

  ```bash
  conda info --envs
  
  base                     C:\Users\ultra\Anaconda3
  cv_env                   C:\Users\ultra\Anaconda3\envs\cv_env
  data_env                 C:\Users\ultra\Anaconda3\envs\data_env
  gpu_env                  C:\Users\ultra\Anaconda3\envs\gpu_env
  ocr_env               *  C:\Users\ultra\Anaconda3\envs\ocr_env
  py27                     C:\Users\ultra\Anaconda3\envs\py27
  ```

  - 가상환경 삭제

  ```bash
  conda remove --name ocr_env --all
  ```

  - 가상환경을 kernel에 추가해주기

    - install nb_conda

    ```bash
    conda install -c anaconda nb_conda
    ```

    - kernel에 추가

    ```bash
    python -m ipykernel  install  --user --name ocr_env
    ```

  - jupyter notebook work space관리 위한 환경설정 파일 생성

  ```bash
  jupyter notebook --generate-config
  ```

  - 나오게되는 경로 확인하고 그 파일에서
    - `c.NotebookApp.notebook_dir =  ‘’`부분 주석처리 지우고 원하는 경로 기입

  

- install tensorflow-gpu

  ```bash
  conda install tensorflow-gpu
  ```

  - `pip`로 install하면 DLL error날 수도있음

  - gpu check

  ```bash
  python
  >>> from tensorflow.python.client import device_lib
  >>> print(device_lib.list_local_devices())
  
  Created TensorFlow device (/device:GPU:0 with 1365 MB memory) -> physical GPU (device: 0, name: GeForce MX150, pci bus id: 0000:01:00.0, compute capability: 6.1)
  [name: "/device:CPU:0"
  device_type: "CPU"
  memory_limit: 268435456
  locality {
  }
  incarnation: 12351599525420600458
  , name: "/device:GPU:0"
  device_type: "GPU"
  memory_limit: 1431440179
  locality {
    bus_id: 1
    links {
    }
  }
  incarnation: 16028943313971802923
  physical_device_desc: "device: 0, name: GeForce MX150, pci bus id: 0000:01:00.0, compute capability: 6.1"
  ```

  



