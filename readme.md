create a program which takes random sequence of numbers and letters
(example: 'dfssdfsdfsdf655sdf2654fs6d4646').

The program sgould return (All stages requires separate functions, with logging all necessary data to file and error handling):
1) list of letters ordered
2) list of letters of reversed order
3) funtion which return list with only uniques letters (Can't repeat)
4) the same do with numbers
5)the sum of amount of letters and numbers are provided

Rules:The program after text entered, should provide options list of actions:
1) Get list ordered
2) Get list ordered reversed etc...

If there is special symbols,gaps - they should be added to special data structure,
as we will have option :n) Show special symbols if provided.After any option
is being used, terminal should ask if we want to use another option or to exit
the program.If we choose to use another option, the option we already choose
should be marked as `checked`:
1) Get list ordered[checked]
sequence length should be nor less than 25 characters 