# overloading example


def details(name,number,role=None):

    if role != None:
        print("my name is :",name)
        print("my contact number is :",number)
        print("my disignation is :",role)
    else:
        print("my name is :",name)
        print("my contact number is :",number)

details("sowje",9014567636,"python")
print("-----------------------------")
details("siva",9014141105,"python")