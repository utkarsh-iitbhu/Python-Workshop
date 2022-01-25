import numpy as np
import Python_Exercises
funcs = [Python_Exercises.power, Python_Exercises.split_str, Python_Exercises.format,
         Python_Exercises.indexing , Python_Exercises.subjective, Python_Exercises.dictionary, Python_Exercises.domainGet,
         Python_Exercises.findDog, Python_Exercises.countDog, Python_Exercises.lambdafunc, Python_Exercises.caught_speeding]
debug = False
test_cases = {
              'power' : [
                        [(7,4),2401]
                        ],
              'split_str' : [
                         [("Hi there Sam!",),["Hi","there","Sam!"]]
              ],
         
              'format' : [
                          [("Earth",12742,),'The diameter of Earth is 12742 kilometers.']
              ],
         
         'indexing' : [
    [
         ([1,2,[3,4],[5,[100,200,["hello"]],23,11],1,7],) , 
            
         ("hello")
                    
              ]
    ],
                  'subjective' : [['',"immutable"]],
              

                  'dictionary' : [
                                  [({'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]},),
                                  ("hello")]
                                  ],
                  

              'domainGet' : [
                              [('user@domain.com',),'domain.com']
                                ],
              'findDog' : [
                              [('Is there a dog here?',),True]
                                    ],
              'countDog' : [
                            [('This dog runs faster than the other dog dude!',),2]
                            ],
              'lambdafunc' : [[ (['soup','dog','salad','cat','great'],),
                              ['soup','salad'],
              ]],
              'caught_speeding' : [
                                   [(81,True),"Small Ticket"]
              ]
             }     ## Will be filled after submission date

score = 0

for func in funcs:
    flag = 1
    for i,test_case in enumerate(test_cases[func.__name__]):
        
        x, y = test_case

        try:
            if func.__name__ == 'eqn_solver':
                np.testing.assert_allclose( y, func(*x) )

            else:
                
                assert y==func(*x)
                
        except Exception as e:
            print(e)
            flag = 0
            print("function "+func.__name__+" fails on testcase "+str(i+1),end="")
            if debug:
                print("because ")
                
            else:
                print("")
    if flag==1:
        print("function "+func.__name__+" passes all the test cases!")
    score += flag

print("Your score is "+str(score)+"!!,\nYou will receive extra points for smart implementation directly on the pull request")
if score!=len(funcs):
    raise Exception("Did not pass all tests")
