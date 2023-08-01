# DRF 구현 4차 재시작

 ## 해당 README.md는 해당 Repo의 작업 진행만을 작성했습니다. 프로젝트의 전체적인 진행은 https://github.com/tosecfromback/DRF_Back/wiki 을 참고 부탁드립니다.
 
 ## 23.08.01 
  ### PM 13:15 가상환경부터 구성시작
  ### PM 13:56 기본 구성(파일구조, urls, views 기본 값으로 구조 확인)
  ### PM 14:27 각 App의 models.py 기본 구성
   #### PM 14:36 gpt와 post app 간의 연동 에러
   ```shell
   ImportError: attempted relative import beyond top-level package
   ```
   ```python
   from ..gpt.models import QnA
   
   from gpt.models impost QnA
   ```
   - python의 파일구조 설정 실수, 2번째 python코드와 같이 수정 후 해결
   
   #### PM 14:43 gpt와 post App 같의 단일 class를 2개 이상 참조하는 과정에서 TypeError 발생
   ```shell
   TypeError: ForeignKey(<django.db.models.query_utils.DeferredAttribute object at 0x00000205CC1DCA10>) is invalid. First parameter to ForeignKey must be either a model, a model name, or the string 'self'
   ```
   
   #### PM 15:08 Post App의 Model은 GPT App의 Model과 1:1관계를 갖고있을 예정이므로 해당 Model을 참조하는 것으로 DB의 자원을 아끼는 것이 가능하므로 Post App의 불필요한 Model은 구성하지 않는 방향으로 진행
    - 만약 1:N의 관계로 구성을 진행 할 경우 ForeignKey의 첫 번째 인자는 'class 모델명'으로 제한되므로 가져오려는 모델과 같은 모델을 만들어서 하위 컬럼으로 값을 가져오는 방향으로 가능함