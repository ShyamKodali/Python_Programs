# Lambda function usage with example

def func(x):
    fn = lambda y:x+23
    return fn(x)

print(func(20))