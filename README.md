# c0de_gr1nd
the pursuit of ameloriation as a programmer

<img src="https://i.imgur.com/2GJnHcq.gif" width="420" height="302">

## Introduction
* This repository features my solutions and explanations to the problems presented in </br>
  [Elements of Programming Interviews in Python](http://bit.ly/epipython)
* The book solutions and test framework are from [EPI Judge](https://github.com/adnanaziz/EPIJudge)
* The descriptions of the problems are excerpts from the EPI book.

## Primitive Types
| # | Title | Solution | Time | Space |
|---|-------|----------|------|-------|
|4.1|[Computing the Parity of a Word](./python_explanations/parity.md)|[Python](./python_solutions/parity.py)|_O(logn)_|_O(1)_|
|4.2|[Swap Bits](./python_explanations/swap_bits.md)|[Python](./python_solutions/swap_bits.py)|_O(1)_|_O(1)_|
|4.3|[Reverse Bits](./python_explanations/reverse_bits.md)|[Python](./python_solutions/reverse_bits.py)|_O(n)_|_O(1)_|
|4.4|[Find a Closest Integer with the Same Weight](./python_explanations/closest_int_same_weight.md)|[Python](./python_solutions/closest_int_same_weight.py)|_O(n)_|_O(1)_|
|4.5|[Compute _x_ &times; _y_ Without Arithmetical Operators](./python_explanations/primitive_multiply.md)|[Python](./python_solutions/primitive_multiply.py)|_O(n)_|_O(n<sup>2</sup>)_|
|4.6|[Compute _x_ &#8725; _y_](./python_explanations/primitive_divide.md)|[Python](./python_solutions/primitive_divide.py)|_O(n)_|_O(1)_|
|4.7|[Compute _x <sup>y</sup>_](./python_explanations/power_x_y.md)|[Python](./python_solutions/power_x_y.py)|_O(n)_|_O(1)_|
|4.8|[Reverse Digits](./python_explanations/reverse_digits.md)|[Python](./python_solutions/reverse_digits.py)|_O(n)_|_O(1)_|
|4.9|[Check If a Decimal Integer Is a Palindrome](./python_explanations/is_number_palindromic.md)|[Python](./python_solutions/is_number_palindromic.py)|_O(n)_|_O(1)_|
|4.10|[Generate Uniform Random Numbers](./python_explanations/uniform_random_number.md)|[Python](./python_solutions/uniform_random_number.py)|_O(logn)_|_O(1)_|
|4.11|[Rectangle Intersection](./python_explanations/rectangle_intersection.md)|[Python](./python_solutions/rectangle_intersection.py)|_O(1)_|_O(1)_|

## Arrays
| # | Title | Solution | Time | Space |
|---|-------|----------|------|-------|
|5.1|[The Dutch National Flag Problem](./python_explanations/dutch_national_flag.md)|[Python](./python_solutions/dutch_national_flag.py)|_O(n)_|_O(1)_|
|5.2|[Increment an Arbitrary-Precision Integer](./python_explanations/int_as_array_increment.md)|[Python](./python_solutions/int_as_array_increment.py)|_O(n)_|_O(1)_|
|5.3|[Multiply Two Arbitrary-Precision Integers](./python_explanations/int_as_array_multiply.md)|[Python](./python_solutions/int_as_array_multiply.py)|_O(nm)_|_O(n+m)_|
|5.4|[Advancing Through an Array](./python_explanations/advance_by_offsets.md)|[Python](./python_solutions/advance_by_offsets.py)|_O(n)_|_O(1)_|
|5.5|[Delete Duplicates from a Sorted Array](./python_explanations/sorted_array_remove_dups.md)|[Python](./python_solutions/sorted_array_remove_dups.py)|_O(n)_|_O(1)_|
|5.6|[Buy and Sell a Stock Once](./python_explanations/buy_and_sell_stock.md)|[Python](./python_solutions/buy_and_sell_stock.py)|_O(n)_|_O(1)_|
|5.7|[Buy and Sell a Stock Twice](./python_explanations/buy_and_sell_stock_twice.md)|[Python](./python_solutions/buy_and_sell_stock_twice.py)|_O(n)_|_O(n)_|
|5.8|[Computing an Alternation](./python_explanations/alternating_array.md)|[Python](./python_solutions/alternating_array.py)|_O(n)_|_O(1)_|
|5.9|[Enumerate All Primes to _n_](./python_explanations/prime_sieve.md)|[Python](./python_solutions/prime_sieve.py)|_O(nloglogn)_|_O(n)_|
|5.10|[Permute the Elements of an Array](./python_explanations/apply_permutation.md)|[Python](./python_solutions/apply_permutation.py)|_O(n)_|_O(n)_|
|5.11|[Compute the Next Permutation](./python_explanations/next_permutation.md)|[Python](./python_solutions/next_permutation.py)|_O(n)_|_O(1)_|
|5.12|[Sample Offline Data](./python_explanations/offline_sampling.md)|[Python](./python_solutions/offline_sampling.py)|_O(k)_|_O(1)_|
|5.13|[Sample Online Data](./python_explanations/online_sampling.md)|[Python](./python_solutions/online_sampling.py)|_O(n)_|_O(k)_|
|5.14|[Compute a Random Permutation](./python_explanations/random_permutation.md)|[Python](./python_solutions/random_permutation.py)|_O(n)_|_O(1)_|
|5.15|[Compute a Random Subset](./python_explanations/random_subset.md)|[Python](./python_solutions/random_subset.py)|_O(k)_|_O(k)_|
|5.16|[Generate Nonuniform Random Numbers](./python_explanations/nonuniform_random_number.md)|[Python](./python_solutions/nonuniform_random_number.py)|_O(n)_|_O(n)_|
|5.17|[The Sudoku Checker Problem](./python_explanations/is_valid_sudoku.md)|[Python](./python_solutions/is_valid_sudoku.py)|_O(n<sup>2</sup>)_|_O(n)_|
|5.18|[Compute the Spiral Ordering of a 2D Array](./python_explanations/spiral_ordering_segments.md)|[Python](./python_solutions/spiral_ordering_segments.py)|_O(n<sup>2</sup>)_|_O(n)_|
|5.19|[Rotate a 2D Array](./python_explanations/matrix_rotation.md)|[Python](./python_solutions/matrix_rotation.py)|_O(n<sup>2</sup>)_|_O(1)_|
|5.20|[Compute Rows in Pascal's Triangle](./python_explanations/pascal_triangle.md)|[Python](./python_solutions/pascal_triangle.py)|_O(n<sup>2</sup>)_|_O(n<sup>2</sup>)_|

## Strings
| # | Title | Solution | Time | Space |
|---|-------|----------|------|-------|
|6.1|[Interconvert Strings and Integers](./python_explanations/string_integer_interconversion.md)|[Python](./python_solutions/string_integer_interconversion.py)|_O(n)_|_O(n)_|
|6.2|[Base Conversion](./python_explanations/convert_base.md)|[Python](./python_solutions/convert_base.py)|_O(nlogn)_|_O(n)_|
|6.3|[Compute the Spreadsheet Column Encoding](./python_explanations/spreadsheet_encoding.md)|[Python](./python_solutions/spreadsheet_encoding.py)|_O(n)_|_O(n)_|
|6.4|[Replace and Remove](./python_explanations/replace_and_remove.md)|[Python](./python_solutions/replace_and_remove.py)|_O(n)_|_O(1)_|
|6.5|[Test Palindromicity](./python_explanations/is_string_palindromic_punctuation.md)|[Python](./python_solutions/is_string_palindromic_punctuation.py)|_O(n)_|_O(1)_|
|6.6|[Reverse All the Words in a Sentence](./python_explanations/reverse_words.md)|[Python](./python_solutions/reverse_words.py)|_O(n)_|_O(1)_|
|6.7|[Compute All Mnemonics for a Phone Number](./python_explanations/phone_number_mnemonic.md)|[Python](./python_solutions/phone_number_mnemonic.py)|_O(4<sup>n</sup>n)_|_O(n)_|
|6.8|[The Look-and-Say Problem](./python_explanations/look_and_say.md)|[Python](./python_solutions/look_and_say.py)|_O(n2<sup>n</sup>)_|_O(2<sup>n</sup>)_|
|6.9|[Convert from Roman to Decimal](./python_explanations/roman_to_integer.md)|[Python](./python_solutions/roman_to_integer.py)|_O(n)_|_O(1)_|
|6.10|[Compute All Valid IP Addresses](./python_explanations/valid_ip_addresses.md)|[Python](./python_solutions/valid_ip_addresses.py)|_O(1)_|_O(1)_|
|6.11|[Write a String Sinusoidally](./python_explanations/snake_string.md)|[Python](./python_solutions/snake_string.py)|_O(n)_|_O(1)_|
|6.12|[Implement Run-Length Encoding](./python_explanations/run_length_compression.md)|[Python](./python_solutions/run_length_compression.py)|_O(n)_|_O(n)_|
|6.13|[Find the First Occurrence of a Substring](./python_explanations/substring_match.md)|[Python](./python_solutions/substring_match.py)|_O(n+m)_|_O(1)_|

## Linked Lists
| # | Title | Solution | Time | Space |
|---|-------|----------|------|-------|
|7.1|[Merge Two Sorted Lists](./python_explanations/sorted_lists_merge.md)|[Python](./python_solutions/sorted_lists_merge.py)|_O(n+m)_|_O(1)_|
|7.2|[Reverse a Single Sublist](./python_explanations/reverse_sublist.md)|[Python](./python_solutions/reverse_sublist.py)|_O(n)_|_O(1)_|
|7.3|[Test for Cyclicity](./python_explanations/is_list_cyclic.md)|[Python](./python_solutions/is_list_cyclic.py)|_O(n)_|_O(1)_|
|7.4|[Test for Overlapping Lists&mdash;Lists Are Cycle-Free](./python_explanations/do_terminated_lists_overlap.md)|[Python](./python_solutions/do_terminated_lists_overlap.py)|_O(n)_|_O(1)_|
|7.5|[Test for Overlapping Lists&mdash;Lists May Have Cycles](./python_explanations/do_lists_overlap.md)|[Python](./python_solutions/do_lists_overlap.py)|_O(n)_|_O(1)_|
|7.6|[Delete a Node from a Singly Linked List](./python_explanations/delete_node_from_list.md)|[Python](./python_solutions/delete_node_from_list.py)|_O(1)_|_O(1)_|
|7.7|[Remove the *k*th Last Element from a List](./python_explanations/delete_kth_last_from_list.md)|[Python](./python_solutions/delete_kth_last_from_list.py)|_O(n)_|_O(1)_|
|7.8|[Remove Duplicates from a Sorted List](./python_explanations/remove_duplicates_from_sorted_list.md)|[Python](./python_solutions/remove_duplicates_from_sorted_list.py)|_O(n)_|_O(1)_|
|7.9|[Implement Cyclic Right Shift for Singly Linked Lists](./python_explanations/list_cyclic_right_shift.md)|[Python](./python_solutions/list_cyclic_right_shift.py)|_O(n)_|_O(1)_|
|7.10|[Implement Even-Odd Merge](./python_explanations/even_odd_list_merge.md)|[Python](./python_solutions/even_odd_list_merge.py)|_O(n)_|_O(1)_|
|7.11|[Test Whether a Singly Linked List Is Palindromic](./python_explanations/is_list_palindromic.md)|[Python](./python_solutions/is_list_palindromic.py)|_O(n)_|_O(1)_|
|7.12|[Implement List Pivoting](./python_explanations/pivot_list.md)|[Python](./python_solutions/pivot_list.py)|_O(n)_|_O(1)_|
|7.13|[Add List-Based Integers](./python_explanations/int_as_list_add.md)|[Python](./python_solutions/int_as_list_add.py)|_O(n+m)_|_O(max(n,m))_|

## Stacks and Queues
| # | Title | Solution | Time | Space |
|---|-------|----------|------|-------|
|8.1|[Implement a Stack with Max API](./python_explanations/stack_with_max.md)|[Python](./python_solutions/stack_with_max.py)|_O(1)_|_O(n)_|
|8.2|[Evaluate RPN Expressions](./python_explanations/evaluate_rpn.md)|[Python](./python_solutions/evaluate_rpn.py)|_O(n)_|_O(n)_|
|8.3|[Test a String over "{,},(,),[,]" for Well-Formedness](./python_explanations/is_valid_parenthesization.md)|[Python](./python_solutions/is_valid_parenthesization.py)|_O(n)_|_O(n)_|
|8.4|[Normalize Pathnames](./python_explanations/directory_path_normalization.md)|[Python](./python_solutions/directory_path_normalization.py)|_O(n)_|_O(n)_|
|8.5|[Compute Buildings with a Sunset View](./python_explanations/sunset_view.md)|[Python](./python_solutions/sunset_view.py)|_O(n)_|_O(n)_|
|8.6|[Compute Binary Tree Nodes in Order of Increasing Depth](./python_explanations/tree_level_order.md)|[Python](./python_solutions/tree_level_order.py)|_O(n)_|_O(n)_|
|8.7|[Implement a Circular Queue](./python_explanations/circular_queue.md)|[Python](./python_solutions/circular_queue.py)|_O(1)_|_O(n)_|
|8.8|[Implement a Queue Using Stacks](./python_explanations/queue_from_stacks.md)|[Python](./python_solutions/queue_from_stacks.py)|_O(1)_|_O(n)_|
|8.9|[Implement a Queue with Max API](./python_explanations/queue_with_max.md)|[Python](./python_solutions/queue_with_max.py)|_O(1)_|_O(n)_|

## Binary Trees
| # | Title | Solution | Time | Space |
|---|-------|----------|------|-------|
|9.1|[Test If a Binary Tree Is Height-Balanced](./python_explanations/is_tree_balanced.md)|[Python](./python_solutions/is_tree_balanced.py)|_O(n)_|_O(h)_|
|9.2|[Test If a Binary Tree Is Symmetric](./python_explanations/is_tree_symmetric.md)|[Python](./python_solutions/is_tree_symmetric.py)|_O(n)_|_O(h)_|
|9.3|[Compute the Lowest Common Ancestor in a Binary Tree](./python_explanations/lowest_common_ancestor.md)|[Python](./python_solutions/lowest_common_ancestor.py)|_O(n)_|_O(h)_|
|9.4|[Compute the LCA When Nodes Have Parent Pointers](./python_explanations/lowest_common_ancestor_with_parent.md)|[Python](./python_solutions/lowest_common_ancestor_with_parent.py)|_O(h)_|_O(1)_|
|9.5|[Sum the Root-To-Leaf Paths in a Binary Tree](./python_explanations/sum_root_to_leaf.md)|[Python](./python_solutions/sum_root_to_leaf.py)|_O(n)_|_O(h)_|
|9.6|[Find a Root to Leaf Path with Specified Sum](./python_explanations/path_sum.md)|[Python](./python_solutions/path_sum.py)|_O(n)_|_O(h)_|
|9.7|[Implement an Inorder Traversal Without Recursion](./python_explanations/tree_inorder.md)|[Python](./python_solutions/tree_inorder.py)|_O(n)_|_O(h)_|
|9.8|[Implement a Preorder Traversal Without Recursion](./python_explanations/tree_preorder.md)|[Python](./python_solutions/tree_preorder.py)|_O(n)_|_O(h)_|
|9.9|[Compute the *k*th Node in an Inorder Traversal](./python_explanations/kth_node_in_tree.md)|[Python](./python_solutions/kth_node_in_tree.py)|_O(h)_|_O(1)_|
|9.10|[Compute the Successor](./python_explanations/successor_in_tree.md)|[Python](./python_solutions/successor_in_tree.py)|_O(h)_|_O(1)_|
|9.11|[Implement an Inorder Traversal with _O(1)_ Space](./python_explanations/tree_with_parent_inorder.md)|[Python](./python_solutions/tree_with_parent_inorder.py)|_O(n)_|_O(1)_|

<!---
|9.BLANK|[BLANK](./python_explanations/BLANK.md)|[Python](./python_solutions/BLANK.py)|_O(BLANK)_|_O(BLANK)_|
-->

## Random Code &mdash; Not from EPI
| Title | Solution | Time | Space |
|-------|----------|------|-------|
|[Shiba](./random_code/shiba/README.md)|[ASM](./random_code/shiba/shiba.asm)|_O(w0w)_|_O(such)_|
|[Caesar Cipher](./random_code/caesar_cipher/README.md)|[Python](./random_code/caesar_cipher/caesar_cipher.py)|_N/A_|_N/A_|
|[FizzBuzz](./random_code/fizz_buzz/README.md)|[Python](./random_code/fizz_buzz/fizzbuzz.py) </br> [C++](./random_code/fizz_buzz/fizzbuzz.cpp) </br> [ASM](./random_code/fizz_buzz/fizzbuzz.asm)|_O(n)_|_O(1)_|

## Useful References
* [Big-O Cheat Sheet](http://www.bigocheatsheet.com/)
* [Python Wiki - Time Complexity](https://wiki.python.org/moin/TimeComplexity)
* [Python Code Visualizer](http://www.pythontutor.com/visualize.html#mode=edit)
* [Python Tutorial](https://www.tutorialspoint.com/python/)
* [Open Data Structures](https://opendatastructures.org/)
* [Problem Solving with Algorithms and Data Structures using Python](http://www.openbookproject.net/books/pythonds/index.html)
* [Big O Notation and Algorithm Analysis with Python Examples](https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/)

## Acknowledgements
* [Adnan Aziz](https://github.com/adnanaziz) - Author of EPI
* [Tsung-Hsien Lee](https://github.com/tsunghsienlee) - Author of EPI
* Amit Prakash - Author of EPI
* All contributers to the [EPI Judge](https://github.com/adnanaziz/EPIJudge)
* [Brandon Hough](https://github.com/insomniac94) - Incubate distributed infomediaries
* [Cory Walker](https://github.com/corywalker) - Mesh distributed mindshare

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details