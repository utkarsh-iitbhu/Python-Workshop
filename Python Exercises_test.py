import numpy as np
funcs = [power, split, format, domainGet, findDog, countDog, lambdafunc, caught_speeding]
debug = False
test_cases = {
              'power' : [
                        [(7,4),2401]
                        ],
              'split' : [
                         ["Hi there Sam!",["Hi","there","Sam!"]]
              ],
              'format' : [
                          [('Earth',12742),"The diameter of Earth is 12472 kilometers."]
              ],

              'domainGet' : [
                              ['user@domain.com','user@domain.com'']
                                ],
              'findDog' : [
                              ['Is there a dog here?',True]
                                    ],
              'countDog' : [
                            ['This dog runs faster than the other dog dude!',2]
                            ],
              'lambdafunc' : [ ['soup','dog','salad','cat','great'],
                              ['soup','salad'],
                              ],
              'caught_speeding' : [
                                   [(81,True),Small Ticket]
              ]
             }     ## Will be filled after submission date

score = 0

for func in funcs:
    flag = 1
    for i,test_case in enumerate(test_cases[func._name_]):
        x, y = test_case
        try:
            assert y==func(*x)
        except Exception as e:
            flag = 1
            print("function "+func._name_+" fails on testcase "+str(i+1),end="")
            if debug:
                print("because ")
                print(e)
            else:
                print("")
    score += flag

print("Your score is "+str(score)+"!!, You will receive extra points for smart implementation directly in the pull request")
