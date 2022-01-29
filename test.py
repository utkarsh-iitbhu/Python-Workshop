import numpy as np
import Python_Exercises 
funcs = [Python_Exercises.power, Python_Exercises.split_str, Python_Exercises.format,
         Python_Exercises.indexing , Python_Exercises.subjective, Python_Exercises.dictionary, Python_Exercises.domainGet,
         Python_Exercises.findDog, Python_Exercises.countDog, Python_Exercises.lambdafunc, Python_Exercises.caught_speeding,
         Python_Exercises.create_arr_of_fives,Python_Exercises.even_num,Python_Exercises.create_matrix,
         Python_Exercises.linear_space,Python_Exercises.decimal_mat,Python_Exercises.slices_1,Python_Exercises.slices_2,Python_Exercises.slices_3]
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
              ],
         
           'create_arr_of_fives': [
                                      ['', (([ 5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.,  5.]))
              ]
              ],

              'even_num': [
                           ['',([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
       44, 46, 48, 50])]
              ],

            'create_matrix' : [
                               [
                                '',(([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]]))
                               ]
            ],

          'linear_space' : [
                            [
                             '',(([0.0,
 0.05263157894736842,
 0.10526315789473684,
 0.15789473684210525,
 0.21052631578947367,
 0.2631578947368421,
 0.3157894736842105,
 0.3684210526315789,
 0.42105263157894735,
 0.47368421052631576,
 0.5263157894736842,
 0.5789473684210527,
 0.631578947368421,
 0.6842105263157894,
 0.7368421052631579,
 0.7894736842105263,
 0.8421052631578947,
 0.894736842105263,
 0.9473684210526315,
 1.0])
                             )]
          ],

          'decimal_mat': [
                          [
                           '',([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])
                          ]
          ],

          'slices_1': [['',([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])
          ]],

          'slices_2' : [[
             '',([[ 2],
       [ 7],
       [12]])
          ]],

          'slices_3' : [[
               '',([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
          ]]

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
