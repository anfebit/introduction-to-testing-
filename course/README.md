# Testing using Python

Pytest and some functionalities


# What is unitesting? 

It is one of the many techniques for software testing to test the smallest piece of code that can be isolated, for example, a function (method if it is within a class)

Some of the types of testing that are used in a project are as follow

![image](https://user-images.githubusercontent.com/607102/178393131-44c02144-65ac-4513-b1b0-aa03f07b79de.png)


## Why do we need testing? 

- Identify bugs easily and early
- Help you write better code
- Test at a low cost
- Serve as documentation

## How to write down a good unit test?
**Independent:** the test focuses on the functionality and it is independent of any API call, DB connection, and external services. Most of the dependencies should be mocked.

**Repeatable:** no matter how many times you run the test, the results should be always the same.
What is mocked?. Creating a fake version of an external or internal service that can stand in for the real one.

**Consistent and readable:** if the testing looks convoluted or hard to understand, it might mean that the function/method was not well written. I would like to recall the KISS principle. Keep It Simple, Stupid and the single responsibility principle, which states that every class or module in a program should only provide one specific functionality.

**Automatic:** the process of running the unitest should be integrated into CI/CD tools, in this way quality code will be always ensured.

**Coverage:** cover as much as you can of your code, most programming languages provide coverage tools. 

## Key concepts while testing using Python

**- Mock**  
**- Fixture**  
**- Parametrizing**  
**- Side Effects**  
