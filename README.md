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
    
    !img](img/2.png)
  
  - 분명히 parameter 'source'의 값을 넣어주고 테스트를 했음에도 불구하고 오류코드 N2MT01 ( parameter 'source'가 없을때 뜨는 오류)가 계속 나오는것입니다
  
  - 반면에 코드로 API호출을 했을때는 문제 없이 값을 반환하는것을 볼 수 있었습니다.
  
    ![img](img/1.png)
    
   - 결론적으로 찾은 문제점은 포스트맨에서는 한글을 잘 못읽는다는 것입니다. (헤결완료)

***
  
  - Intertranslatable language in this code
  
    - Korean <-> English
    
    - Korean <-> Japanese
    
    - Korean <-> Chinese(Simplified Chinese)
  
  - ![img](https://scontent-ssn1-1.xx.fbcdn.net/v/t1.0-9/91406580_1166382357038329_5127730578174509056_n.jpg?_nc_cat=100&_nc_sid=8024bb&_nc_ohc=L7ztVaRi6fYAX9LA6GD&_nc_ht=scontent-ssn1-1.xx&oh=b0d750ddd50ba5489714d276f81a8910&oe=5EA9A6A3)
  - ![img](https://scontent-ssn1-1.xx.fbcdn.net/v/t1.0-9/90386514_1166382533704978_5624512651980701696_n.jpg?_nc_cat=110&_nc_sid=8024bb&_nc_ohc=-f7wX1GdCjYAX8ka-TD&_nc_ht=scontent-ssn1-1.xx&oh=32ca4f0d3183ca8e803fa360f5691e94&oe=5EA6F162)
  - ![img](https://scontent-ssn1-1.xx.fbcdn.net/v/t1.0-9/91033126_1166382857038279_7303358017288798208_n.jpg?_nc_cat=107&_nc_sid=8024bb&_nc_ohc=x3_k8-A8WRAAX8uiVWc&_nc_ht=scontent-ssn1-1.xx&oh=50dca9947b8e370f4606e3045e416d75&oe=5EA8D9FE)
  
  
