"""
AUTHOR: TANMAY MUDGAL
PROJECT: QUIZ MASTER

This project is about quiz management system which provides functionality of creating, managing and playing quizzes.
It includes features such as filtering of quizzes, leaderboards of other users and quizzes and many more.

There are three roles:
    1. Player: Can play quizzes.
    2. Creator: Can manage their own quizzes.
    3. Admin: Will manage users(and maybe quizzes in the future, like can remove them).

The implementation contains not only the core functionality of the app but also security of the application with,
    1. RBAC
    2. Proper Logging
    3. Password Hashing
    And many more.

Doc-Strings are only provided where they are necessary and required to understand the functionality working.
Don't use Doc-Strings such as,
    This class will handle authentication logic.
Use such a class name that it's self understood.

For each package in this project __init__ files are used for,
    1. Explaining usage of the package or the sub files in the package.
    2. Future scope of the package.
    3. Why things are the way they are in the package.
    4. What are the convention for this project.

Rules for this project:
    1. No one will stop you from using magic methods. Remember they are magic methods not pills.
    2. Just because it looks different doesn't mean it's not a good approach.
    3. If it's hard to explain then, mostly it's a bad approach.
    4. If it's too easy to explain, then maybe it's a good approach.
    5. If it's optimised without breaking the conventions of the project use it.
    6. If it's optimised but break some conventions of the project,
        1. Use it only if the optimisation is really great
        2. Or the whole project could be restructured in the new convention and will not degrade the performance.
    7. If you can't follow clean code principles, then you are not ready yet to code.
    8. If you are not patient and calm while writing code, then you are not ready yet to code.
    9. Python is flexible for our benefit, use it in good way and don't just do random stupid things.
    10. Just because it could be done, don't mean it should be done.
    NOTE: These conventions I talk of are nothing but the underlying pattern in each module of this project.

Always remember this project is created in such a way that each package, module and class is following OOPS and SOLID.
In some places OOPS and SOLID may not be followed but those places are exceptions and following OOPS and SOLID will only
degrade the code quality.
OOPS, and SOLID are used to make better project architecture, they are not be followed just for the sake of following.

LIFE RULE: In case of any confusion try to understand the pattern. Or contact the creator.

LEARNINGS:
    1. Using pythonic singleton approach is quite good and have its own benefits.
        But remember that it is really hard to control its creation.
        You should have control over things when they are created and when they are destroyed.
    2. Even if you like to try new things out always try to see the bigger picture.
    3. Yes, some approaches may look good and easy to implement, but they can create a lot of problems later on.
    4. Experience is what's you'll get while doing various things.

Future Scope:
    I want to create a framework on the top of flask which will provide a structured architecture for Flask Web APIs.
    There is no reason to pretend to be cool. Let's show our lame sides. That's who we really are, after all.
    What I have is not a dream, because I'll make it reality!
"""
