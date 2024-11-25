# imgSharpen
三种基本的锐化处理算法  
  
算法设计  
普通拉普拉斯变换：  
使用如下算子来逐个检测边缘  
![image](https://github.com/user-attachments/assets/af8183c5-0851-4ef8-a10e-5e11b8e0daa8)  
根据a的值来决定边缘检测的强度  
最后应用到原图上。  
  
拉普拉斯变换变形：  
使用如下算子来逐个检测边缘  
![image](https://github.com/user-attachments/assets/6f8ed352-e806-42fa-a379-2dea290f7095)  
根据a的值来决定边缘检测的强度  
最后应用到原图上。  
    
拉普拉斯-高斯变换：  
使用如下算子来逐个检测边缘  
![image](https://github.com/user-attachments/assets/2a70d0c1-08d9-4930-9af3-f8c5c7a6a8ae)  
根据a的值来决定边缘检测的强度  
最后应用到原图上。  
