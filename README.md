# FreeD_TEST

## Introduce
주어진 문제를 해결하고 python의 단위 테스트 프레임워크인 unittest를 사용하여  테스트하는 과제입니다. 

[freed-soft-assginment.shop:881](freed-soft-assginment.shop:881)**👈 Enter a demo webpage via browser** to see some examples

## The Problem is...
compute the best way an order can be shipped (called shipments) given
inventory across a set of warehouses


<br/>

## Software development environment

|항목|내용|비고|
|:---:|:---:|:---:|
|OS|Ubuntu-22.04||
|Python|3.10.8||

## Python Package usage

|항목|내용|비고|
|:---:|:---:|:---:|
|sys|| built-in Python module|
|os|| built-in Python module|
|unittest|| built-in Python module|
|collections|| built-in Python module|

<br/>

### Precautions
- you need to set up these things
    - docker-compose, docker
<br/>

## Usage

> via PC...

 - Excute test
```
 $ python Test/test_cases.py
```
 - Run App
```
 $ sudo sudo streamlit run main.py --server.headless=true --server.port 881
```

> via docker... 

1. build docker image
```
 $ docker build -t freed/test:v1_ship .
```
2. docker run
```
 $ docker-compose -f stack.yml up
```
3. enter the localhost:881 via chrome or other browser
```
 localhost:881
```

##  Directory 구조
```
    .
    └── main.py
    └── App
        └── app.py
    └── Test
        └── test_cases.py
```