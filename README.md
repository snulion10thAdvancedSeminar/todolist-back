# 2학기 심화세미나 백엔드 레포지토리  
<br/>

## 백엔드 심화 세미나의 목적
- 백엔드 서버를 빠르게 구축하는 기초를 배우기
- 우리가 구축한 시스템의 품질 관리와 운영에 대한 생각을 시작하기
<br/>  

## 주차별 구성
1주차 (평재)
- 상속, 믹스인
- DRF

2주차 (인규, 나영)
- EC2 배포-1

3주차 (인규, 나영)
- EC2 배포-2
- 네트워크

4주차 (혜민, 평재)
- CI/CD
- Docker
- Code Testing 
<br/>

## 1주차 과제
과제 개요
- 이전에 우리는 이미 몇가지 API 구성 방식을 활용해보았습니다. 또한 drf에서 제공하는 클래스들을 활용해보기도 했습니다. 
- 1주차 세미나에서는 이를 이용해 API를 구현하는 방법을 알려주기 보다는 각 방법이 어떻게 동작하는지와 개발자로서 이를 취사선택할 때 어떤 것들을 고려해야하는지 살펴볼 예정입니다. 
- 이를 위해 여러분에게 미리 drf에서 제공하는 빠르고 편한 api 구성 방식에 대한 힌트를 알려드리고, 이를 Todo 앱 내의 View들에 적용하여 기존 코드를 개선하는 과제를 내드리고자 합니다. 

과제 상세
1. Todo 앱 내에 serializers.py 파일을 만들고, todo 모델에 대한 serializer 클래스를 다음 두 가지 클래스 중 하나를 상속받아 구성하기
  - rest_framework의 serializers 모듈이 제공하는 **Serializer 클래스**
  - 동일 모듈의 **ModelSerializer 클래스**
2. Todo 앱 내에 views.py에 미리 구성해놓은 view 클래스들을 다음 네가지 방식 중 취향껏 선택하여 재구성해보기
  - rest_framework의 views 모듈이 제공하는 **APIView 클래스**를 상속받아 재구성
  - rest_framework의 mixins 모듈이 제공하는 **믹스인 모듈**과 generics 모듈이 제공하는 **GenericAPIView 클래스**를 **다중 상속** 받아 재구성
  - rest_framework의 generics 모듈 내의 **9가지 특수 APIView 클래스**를 상속 받아 재구성
  - rest_framework의 viewsets 모듈이 제공하는 **ModelViewSet 클래스**를 상속 받아 재구성
3. 상속 받은 rest_framework 라이브러리 클래스들의 **내부 로직**을 살펴보면서 우리가 상속 받아 사용하는 클래스의 내부가 어떻게 구현되어있는지 살펴보기 (선택 과제)
4. 기존 기능 이외에도 위의 네가지 방식 중 하나를 사용하여 새로운 기능을 가진 api를 작성해보거나, 기존 api 기능을 확장해보기 (선택 과제)

과제 구현 시 참고하면 좋은 레퍼런스
- Account 앱 내에서 작성한 4주차 코드들
- DRF 공식 문서: https://www.django-rest-framework.org/ (상단 API-Guide의 serializers, views, generic views, viewsets 등 참고) 
- **DRF API 뷰 클래스 관련 정리 블로그: https://ssungkang.tistory.com/m/entry/Django-APIView-Mixins-generics-APIView-ViewSet%EC%9D%84-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90**
- 공식 문서가 제일 좋지만, 아무래도 아직 공식 문서를 살펴보는 것에 익숙하지 않다면 위의 블로그에 구현과 관련된 레퍼런스는 충분히 있다고 생각됩니다. 참고해주세요!

위 과제가 아무리 살펴봐도 너무 힘들다... 라고 하신다면 아래 링크의 DRF 튜토리얼을 한 번 쭉 진행해보고 오시기를 적극 권장드립니다.
- https://www.django-rest-framework.org/tutorial/quickstart/
<br/>

## 1주차 과제 제출 방법
- 본 레포지토리(upstream)를 fork 해주세요
- fork한 개인 레포지토리(origin)을 로컬에서 clone 받아주세요
- [본인 이름]-week[주차]로 미리 구성된 브랜치에서 과제를 수행해주세요(Ex. pyungjae-week1)
- 과제 수행 후, 변경 사항을 origin에 푸시하고 upstream의 동일 브랜치로 pr을 날려주세요
