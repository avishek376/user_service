# user_service

_**Module's Usecase**_

> [!TIP]
> Optional information to help a user be more successful.
> 
> [!NOTE]
> Optional information to help a user be more successful.
> 

[![](https://img.shields.io/badge/github-blue?style=for-the-badge)](https://github.com/hamzamohdzubair/redant)
[![](https://img.shields.io/badge/book-blueviolet?style=for-the-badge)](https://hamzamohdzubair.github.io/redant/)
[![](https://img.shields.io/badge/API-yellow?style=for-the-badge)](https://docs.rs/crate/redant/latest)
[![](https://img.shields.io/badge/Crates.io-orange?style=for-the-badge)](https://crates.io/crates/redant)
[![](https://img.shields.io/badge/Lib.rs-lightgrey?style=for-the-badge)](https://lib.rs/crates/redant)


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
    User will get login by username and password.
    We will check the user's email is verified or not.
    If the email is verified then user will be able to login.

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
    
    

