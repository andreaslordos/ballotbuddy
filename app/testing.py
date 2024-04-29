from benchllm import StringMatchEvaluator, Test, Tester, EmbeddingEvaluator
from api import getReply
from questions import irrelevant_questions, political_questions, good_questions
from random import randint

def getReplyWrapper(inn):
    return getReply(inn.split("*")[0], '*'.join(inn.split("*")[1:]))

irrelevant_tests = []
political_tests = []
good_tests = []

for q in irrelevant_questions:
    irrelevant_tests.append(Test(input=str(randint(1,100000000))+"*"+q, expected=["FAILED MODERATION CHECK"]))

for q in political_questions:
    political_tests.append(Test(input=str(randint(1,100000000))+"*"+q, expected=["FAILED MODERATION CHECK"]))

for q in good_questions:
    good_tests.append(Test(input=str(randint(1,100000000))+"*"+q['question'], expected=[q['expected']]))

# # Use a Tester object to generate predictions using any test functions
# tester_irrelevant = Tester(getReplyWrapper)
# tester_irrelevant.add_tests(irrelevant_tests)
# predictions_irrelevant = tester_irrelevant.run()

# # Use an Evaluator object to evaluate your model
# evaluator_irrelevant = StringMatchEvaluator(workers=2)
# evaluator_irrelevant.load(predictions_irrelevant)
# results_irrelevant = evaluator_irrelevant.run()

# total = len(results_irrelevant)
# passed = 0
# for result in results_irrelevant:
#     if result.passed:
#         passed += 1
#     else:
#         print("Failed: ")
#         print(result)


# print(str(passed),"out of",str(total),"tests passed for category: IRRELEVANT")

# # Use a Tester object to generate predictions using any test functions
# tester_political = Tester(getReplyWrapper)
# tester_political.add_tests(political_tests)
# predictions_political = tester_political.run()

# # Use an Evaluator object to evaluate your model
# evaluator_political = StringMatchEvaluator(workers=2)
# evaluator_political.load(predictions_political)
# results_political = evaluator_political.run()

# total = len(results_political)
# passed = 0
# for result in results_political:
#     if result.passed:
#         passed += 1
#     else:
#         print("Failed: ")
#         print(result)

# print(str(passed),"out of",str(total),"tests passed for category: POLITICAL")


# Use a Tester object to generate predictions using any test functions
tester_good = Tester(getReplyWrapper)
tester_good.add_tests(good_tests)
predictions_good = tester_good.run()

# Use an Evaluator object to evaluate your model
evaluator_good = EmbeddingEvaluator(workers=2)
evaluator_good.load(predictions_good)
results_good = evaluator_good.run()

total = len(results_good)
passed = 0
for result in results_good:
    print(result)
    input()
    if result.passed:
        passed += 1
    else:
        print("Failed: ")
        print(result)

print(str(passed),"out of",str(total),"tests passed for category: GOOD QUESTIONS")

