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


实验3-1.tif

![image](https://github.com/user-attachments/assets/e43f0ea3-35db-4da2-9743-c3f89e1f482a) ![image](https://github.com/user-attachments/assets/7ba0102c-aee6-47c6-acd0-a5ef19b63f3e)  
      原图【左】                  基本拉普拉斯变换【右边】  
![image](https://github.com/user-attachments/assets/a1480daf-ad28-4424-b93c-1b2e8628e123) ![image](https://github.com/user-attachments/assets/2f9d9f26-8cca-43b8-bc65-b05b6f7f73ac)  
拉普拉斯变形【左】                拉普拉斯-高斯【右边】  
可以看到三种锐化算法都能正确的完成任务。  
其中拉普拉斯变形效果最好，对边缘检测效果好，也不会过于敏感。  
而基本拉普拉斯效果不如变形。  
拉普拉斯-高斯虽然更敏感，但是对于噪声敏感，需要预处理.  
