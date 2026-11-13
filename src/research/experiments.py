def parse_jsonl(*, filename):
    print(filename)
    pass

str_list: list[str] = ["a", "b"]

print(str_list)

parse_jsonl(filename = "filename")

def show(*args, **kwargs):
    print(args, kwargs)

print(show(1,2,3))

# lambda syntax
#lambda_test = lambda x: x * 2
#print(lambda_test(4))

# slice stepping rules
slice_a = [10, 20, 30]
#print(slice_a[::0]) # slice step can't be zero, only positive or negative
print(all((1, -1, 0)))

# multiple inner list
list_a = [2,4]
inner_list = [list_a] * 3
print(inner_list)
inner_list[0] = [1,3]
print(inner_list)

# class attributes
class TestClass:
    def __init__(self, colors=None):
        if colors is not None:
            self.colors = colors
    colors = []
instanceA = TestClass()
print(instanceA.colors)
TestClass.colors = ["black"]
instanceB = TestClass(("blue, red"))
print(instanceA.colors)
print(instanceB.colors)
print(TestClass.colors)
