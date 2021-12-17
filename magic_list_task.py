from dataclasses import dataclass


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


# MagicList usage:
# ----------------

@dataclass
class Person:
    age: int = 1


def test_magic_class():
    person_list = MagicList(cls_type=Person)

    person_list[0].age = 6
    print('MagicList of Person, with one person at age 6:', person_list)
    person_list[1] = Person
    print('MagicList of Person, with another person at default age (1):', person_list)

    objects_list = MagicList()
    objects_list[0] = 7
    print('MagicList with one int with value of 7:', objects_list)


def test_enforcing_index_continuity():
    try:
        person_list = MagicList(cls_type=Person)
        person_list[1].age = 6
    except IndexError:
      print('enforcing index continuity test has passed :)')


test_magic_class()
test_enforcing_index_continuity()
