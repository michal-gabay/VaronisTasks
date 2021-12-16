# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class MagicList(list):
    def __init__(self, cls_type=None):
        super().__init__()
        self.cls_type = cls_type

    def __getitem__(self, key):
        if len(self) == key:
            if self.cls_type is not None:
                self.append(self.cls_type())
        return super(MagicList, self).__getitem__(key)

    def __setitem__(self, key, item):
        if len(self) == key:
            if self.cls_type is None:
                self.append(item)
            else:
                self.append(self.cls_type())

        else:
            super(MagicList, self).__setitem__(key, item)


def test_magic_class():
    person_list = MagicList(cls_type=Person)

    person_list[0].age = 6
    print(person_list)
    person_list[1] = Person
    print(person_list)

    int_list = MagicList()
    int_list[0] = 7
    print(int_list)


def test_enforcing_index_continuity():
    try:
        person_list = MagicList(cls_type=Person)
        person_list[1].age = 6
    except IndexError:
      print('enforcing index continuity test has passed :)')


test_magic_class()
test_enforcing_index_continuity()
