"""
Python MixedIn 클래스에만 다중 상속을 사용
http://brownbears.tistory.com/149
"""

class ToDictMixin:
    def to_dict(self):
        """ __dict__ 은 상속받은 value에 대해 dict타입으로 보여줌"""
        print("to_dict", self.__dict__)
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output
    
    def _traverse(self, key, value):
        """ isinstance를 사용한 동적 타입 검사, 인스턴스 딕셔너리 __dict__를 이용한 클래스"""
        if isinstance(value, ToDictMixin):
            print("case 1")
            return value.to_dict()
        elif isinstance(value, dict):
            print("case 2")
            return self._traverse_dict(value)
        elif isinstance(value, list):
            print("case 3")
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            print("case 4")
            return self._traverse_dict(value.__dict__)
        else:
            print("case 5")
            return value

class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)))

print(tree.to_dict())
