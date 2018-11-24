#use Python 3.x

import datetime


def list_compare(list1, list2):
    if len(list1) != len(list2):
        print("Lists are not equal in lengths so they are different")
    else:
        list_equal = []
        print("Comparing data structure type: List")
        log_file.write("\nComparing data structure type: List")
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                list_equal.append(list1[i])
                print("Index %d have different value" %(i))
                print("%s in first list and %s in second list at index %d are not equal" % (list1[i], list2[i], i))
                log_file.write("\nvalue %s in first list and value %s in second list at index %d are not equal" % (list1[i], list2[i], i))
        if any(list_equal):
            print("Input lists are Not equal")
            log_file.write("\nBoth lists are Not equal")
            return False
        else:
            print("Both lists are equal", list1, list2)
            log_file.write("\nBoth lists are equal")
            return True

def dict_compare(dict1, dict2):
    if len(dict1) != len(dict2):
        print("Dictionaries are not equal in lengths so they are different")
    else:
        dict_equal = []
        dict_list1 = list(dict1.keys())
        dict_list2 = list(dict2.keys())
        print("Comparing keys in both the dictionaries first by converting them to lists")
        log_file.write("\nComparing data structure type: Dictionary")
        print(dict_list1)
        print(dict_list2)
        if list_compare(dict_list1, dict_list2):
            print("Keys are equal in given dictionaries. Now comparing values in the dictionaries")
            for i in dict_list1:
                value_type1 = type(dict1[i])
                value_type2 = type(dict2[i])
                if value_type1 == value_type2:
                    if value_type1 == list and list_compare(dict1[i], dict2[i]) is False:
                        #if list_compare(dict1[i], dict2[i]) == False:
                            dict_equal.append(dict1[i])
                            log_file.write("\nvalue %s in first dictionary and value %s in second dictionary at index %s are not equal" % (dict1[i], dict2[i], i))
                            log_file.write("\nInput dictionaries are not equal")
                    elif value_type1 == str and string_compare(dict1[i], dict2[i]) is False:
                        #if string_compare(dict1[i], dict2[i]) == False:
                            dict_equal.append(dict1[i])
                            log_file.write("\nvalue %s in first dictionary and value %s in second dictionary at index %s are not equal" % (dict1[i], dict2[i], i))
                            log_file.write("\nInput dictionaries are not equal")
                else:
                    log_file.write("\nvalue %s in first dictionary and value %s in second string at index %s are not equal" % (dict1[i], dict2[i], i))
                    log_file.write("\nInput dictionaries are not equal")
            if any(dict_equal):
                print("input dictionaries are Not equal")
                log_file.write("\nInput dictionaries are Not equal")
            else:
                print("Both dictionaries are equal", dict1, dict2)
                log_file.write("\nBoth dictionaries are equal")
                return True
        else:
            print("Keys are Not equal in given dictionaries")
            log_file.write("\nKeys are Not equal in given dictionaries so both dictionaries are different")

def string_compare(string1, string2):
    if len(string1) != len(string2):
        print("Strings are not equal in lengths so they are are different")
    else:
        str_equal = []
        print("Comparing data structure type: String")
        log_file.write("\nComparing data structure type: String")
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                str_equal.append(string1[i])
                print("Index %d have different value" %(i))
                print("%s in first string and %s in second string at index %d are not equal" % (string1[i], string2[i], i))
                log_file.write("\nvalue %s in first string and value %s in second string at index %d are not equal" % (string1[i], string2[i], i))
        if any(str_equal):
            print("Input strings are not equal")
            log_file.write("\nInput strings are not equal")
            return False
        else:
            print("Both strings are equal", string1, string2)
            log_file.write("\nBoth strings are equal")
            return True

def find_ds_diff(ds1, ds2):
    if type(ds1) == list and type(ds2) == list:
        list_compare(ds1, ds2)
    elif type(ds1) == dict and type(ds2) == dict:
        dict_compare(ds1, ds2)
    elif type(ds1) == str and type(ds2) == str:
        string_compare(ds1, ds2)
    else:
        print("Data structures provided are unknown or not same")

ds1 = {'a':[1,2,3],'b':[1,2,3],4:"abc"}
ds2 = {'a':[1,2,3],'b':[1,2,3],4:"abc"}
#ds1 = "abcd"
#ds2 = "cjdf"
#ds1 = [1,2,3]
#ds2 = [1,2,4]
print("type(ds1)",type(ds1))
print("type(ds2)",type(ds2))
current_time = str(datetime.datetime.now())
log_file = open("datastructure_compare_log.txt", "a+")
log_file.write("\n\n********* %s ***********" %(current_time))
find_ds_diff(ds1, ds2)
log_file.close()
