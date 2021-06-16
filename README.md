Discord Bot : Translation bot using papago API
===

***
1 . Discord.py Version : 1.0.0(Rewrite Version)

2 . Language : Python3

3 . What for? : Translation bot helps to translate words or sentences more faster with using command

4 . API provided from : [Naver Open API](https://developers.naver.com/main/)

5 . Papago API Documentation : https://developers.naver.com/docs/papago/

6 . Papago API's HTTP Method : POST
***
### The problems I had in writing this code
 
  - 포스트 맨으로 API테스트를 해보던중 이상한 오류가 있었습니다
    
    ![img](img/2.png)
  
  - 분명히 parameter 'source'의 값을 넣어주고 테스트를 했음에도 불구하고 오류코드 N2MT01 ( parameter 'source'가 없을때 뜨는 오류)가 계속 나오는것입니다
  
  - 반면에 코드로 API호출을 했을때는 문제 없이 값을 반환하는것을 볼 수 있었습니다.
  
    ![img](img/1.png)
    
   - 결론적으로 찾은 문제점은 포스트맨에서는 한글을 잘 못읽는다는 것입니다. (헤결완료)

***

- Patch Note

 - 20200629 정기점검 완료 : 상태 : Good

 - 20210404 패치 : 리팩토링 버전으로 업데이트 되었습니다.  리팩토링 전 버전은 [여기](https://github.com/J-hoplin1/Papago-API-Translate-Bot/tree/Before_Refactoring)

***
  
  - Intertranslatable language in this code
  
    - Korean <-> English
    
    - Korean <-> Japanese
    
    - Korean <-> Chinese(Simplified Chinese)
  
  ![img](img/3.jpg)
  ![img](img/4.jpg)
  ![img](img/5.jpg)
  
  
