# Eval_GPT4o_on_SelectiveTest
Eval Performance of GPT-4o on Selective High School Placement Test

To assess the exam capabilities of the current state-of-the-art multimodal model GPT-4o, we selected test questions related to Think Skills from the years 2021 to 2023, sourced from https://education.nsw.gov.au/schooling/students/oc-and-shs/going-to-a-selective-high-school/get-ready-for-the-selective-high-school-placement-test.

Official test questions and answers can be found in the **Selective High School Placement Test** folder.

Processed test questions are available in the **processed** folder.

Code used for evaluation is located in the **code** folder.

Comprehensive test results are detailed in the **results** folder.

Here we provide year-wise analysis and conclusions.

## 2021

1. **Effectiveness of CoT Method**: Answers using the Chain of Thought (CoT) approach showed high consistency with the reference answers, with 22 questions answered correctly. This indicates that the detailed reasoning process of the CoT method significantly improves answer accuracy.

2. **Shortcomings of Vanilla ANS**: Vanilla ANS, or original answers, aligned with the reference answers in only 15 questions. This suggests lower accuracy in answers without detailed reasoning.

3. **Analysis of Errors**:
   - **Lack of Logical Rigor**: Some original answers lacked rigorous logical reasoning, failing to consider all possibilities or conditional constraints.
   - **Inaccurate Information Interpretation**: Some answers did not accurately interpret the information in the questions, leading to answers based on misunderstandings.
   - **Calculation or Analysis Errors**: In questions requiring quantitative analysis, original answers might have been incorrect due to calculation errors or incomplete analysis.

4. **Importance of Problem-Solving Process**: The CoT method emphasizes the importance of the problem-solving process. By systematically analyzing problems, errors can be better identified and corrected.

5. **Educational Insights**: The data suggests that in education, fostering critical thinking and logical reasoning skills is crucial. These skills not only improve answer accuracy but are also essential for lifelong learning.

6. **Role of Artificial Intelligence**: AI shows potential in automatic scoring and providing feedback, but further optimization is needed to ensure accuracy and reliability.

7. **Necessity of Answer Verification**: Despite the improved accuracy with the CoT method, some answers still did not align with the reference answers. This underscores the importance of verifying answers even after detailed reasoning.

In conclusion, the CoT method significantly enhances answer accuracy by providing detailed reasoning processes. However, it also highlights shortcomings in original answer processes. These findings offer valuable insights for educational practices, the development of AI technology, and exam design.

## 2022



1. **Answer Consistency**: In most cases, answers obtained directly through testing (Vanilla ANS) align with those derived using the Chain of Thought (CoT) method (CoT ANS), indicating that CoT can reproduce direct test results in many instances.

2. **Accuracy**: However, there are also cases where the answers from the CoT method (CoT ANS) do not match the reference answers (Ground Truth), suggesting that further optimization of the CoT method may be necessary to improve answer accuracy in certain scenarios.

3. **Problem-Solving Process**: The CoT method typically includes detailed problem-solving steps and logical reasoning, aiding in understanding the process of arriving at answers, which may be lacking in direct testing approaches.

4. **Areas for Improvement**: In some instances, even when the CoT method yields correct answers, there may still be logical gaps or insufficient detail in the problem-solving process, indicating room for improvement in the method.

5. **Special Cases**: For specific questions, such as questions 3 and 4, discrepancies between CoT and direct testing answers were observed, yet the Ground Truth indicated the direct testing answers were correct. This suggests that CoT may introduce additional complexity when handling logically complex or specific reasoning-required questions, potentially leading answers astray.

6. **Educational Significance**: The problem-solving process facilitated by the CoT method holds significant educational value as it demonstrates problem-solving approaches, helping students grasp the logic behind solving problems rather than merely obtaining an answer.

7. **Technological Applications**: Technologically, applying the CoT method can enhance the transparency of problem-solving processes, aiding in the development of more reliable and interpretable artificial intelligence systems.

In summary, while the CoT method often provides correct and logically coherent answers, there is still room for improvement, particularly in handling complex logic and specific types of questions. Combining direct testing with the CoT method may yield more accurate results conducive to learning.

## 2023

1. **Answer Consistency**: In most cases, answers obtained directly through testing (Vanilla ANS) align with those derived using the Chain of Thought (CoT) method (CoT Answer). This suggests that for these questions, GPT-4o produces the same answers regardless of whether CoT strategy is employed.

2. **Accuracy**: However, when comparing CoT answers with the reference answers (Ground Truth), discrepancies were found in some cases. This indicates that in these questions, the CoT strategy may not improve answer accuracy, or in some instances, could introduce errors.

3. **Effectiveness of CoT Strategy**: In some questions, the CoT strategy appears not to alter the answers significantly. This might be because the nature of the questions does not necessitate deep logical reasoning, or GPT-4o is already capable of understanding and answering the questions correctly without CoT.

4. **Error Analysis**:
   - In question 7, the answer C obtained through direct testing matches the CoT answer, but the Ground Truth is D, indicating that CoT strategy did not correct the error in this case.
   - In question 9, answer A obtained through direct testing matches CoT answer B, but the Ground Truth is D, showing that CoT strategy also did not provide the correct answer in this instance.
   - In question 12, answer C obtained through direct testing matches CoT answer A, but the Ground Truth is D, suggesting that CoT strategy might introduce errors in certain scenarios.

5. **Overall Performance**: Looking at the overall data, the CoT strategy provides correct answers in some questions, but it does not consistently outperform answers obtained directly through testing. This variability could be influenced by the complexity of the questions, GPT-4o's comprehension of the questions, and the implementation of the CoT strategy.

6. **Improvement Suggestions**: To enhance the effectiveness of the CoT strategy, further optimization of GPT-4o's logical reasoning capabilities may be necessary. This ensures that the CoT strategy can offer more accurate answers when faced with questions requiring deeper thought.

In summary, while the CoT strategy can be beneficial in certain cases, it is not universally effective. The determination of correct answers may still depend on the nature of the questions, GPT-4o's understanding capabilities, and the specific implementation of the strategy.
