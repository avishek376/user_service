# user_service

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

_**Module's Usecase**_

> [!TIP]
> Optional information to help a user be more successful.
> 
> [!NOTE]
> Optional information to help a user be more successful.
> 






- ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `#f03c15`
- ![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) `#c5f015`
- ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `#1589F0`




`SignUp:`

    1) User will get signup by username,email,password.
    2) Password will be encrypted by Bcrypt password encoding.
    >> Bcrypt is a password hashing function for encrypting the password and getting new password every time.
    >> 2 people having the same password will have different encrypted passwords in DB.

    3) We will send a verification email to the user's email address.
    4) User will verify the email by clicking on the link.
    5) After verification, user will be able to login.
    
`Login:`

    1) User will get login by username and password.
    2) We will check the user's email is verified or not.
    3) If the email is verified then user will be able to login.

`Forgot Password:`
    User will get forgot password by email.
    We will send a reset password link to the user's email address.
    User will reset the password by clicking on the link.

`Change Password:`
    User will get change password by old password and new password.
    We will check the user's old password is correct or not.
    If the old password is correct then we will update the new password.

`Profile:`
    User will get profile by username.
    User will update the profile by username.
    User will delete the profile by username.
    A specific role-based user will get the profile and can change their details based on need.

`Role:`

    1) User will get specific roles set by admin.
    2) Admin will set the roles for the user.
    3) Admin will update the roles for the user.
    4) Admin will delete the roles for the user.
    5) A specific role-based user will get the details of his/her and change it if the role matches.

`Permission:`

    1) User will get specific permissions set by admin.
    2) Admin will set the permissions for the user.
    3) Admin will update the permissions for the user.
    4) Admin will delete the permissions for the user.
    5) A specific role-based user will get the details of his/her and change it if the permission matches.

`User:`

    1) Admin will get all the users.
    2) Admin will create a user.
    3) Admin will update the user.
    4) Admin will delete the user.
    
    

