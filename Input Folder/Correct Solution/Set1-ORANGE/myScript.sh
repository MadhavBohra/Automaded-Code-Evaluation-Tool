#!/bin/bash

# Check if the user has provided any input
if [ $# -eq 0 ]; then
    echo "Please provide either 1,  2 or 3 as input."
    exit 1
fi

# Check if the input is valid (either 1, 2, or 3)
if [[ $1 != 1 && $1 != 2 && $1 != 3 ]]; then
    echo "Invalid input. Please provide either 1, 2, or 3."
    exit 1
fi

current_directory=$(dirname "$0")

# Clean up previous object files and executable
rm -f main.o f1.o f2.o f3.o a.out

# Compile and link main.c with f1.c
if [ $1 -eq 1 ]; then
    gcc -c main.c -o main.o -DF1_COMPILE
    gcc -c f1.c -o f1.o
    gcc main.o f1.o -o a.out
    ./a.out
fi

# Compile and link main.c with f2.c
if [ $1 -eq 2 ]; then
    gcc -c main.c -o main.o -DF2_COMPILE
    gcc -c f2.c -o f2.o
    gcc main.o f2.o -o a.out
    ./a.out
fi

# Compile and link main.c with f3.c
if [ $1 -eq 3 ]; then
    gcc -c main.c -o main.o -DF3_COMPILE
    gcc -c f3.c -o f3.o
    gcc main.o f3.o -o a.out
    ./a.out
fi

# Clean up object files and the final executable
rm -f main.o f1.o f2.o f3.o a.out


# #!/bin/bash

# # Check if the user has provided any input
# if [ $# -eq 0 ]; then
#     echo "Please provide either 1,  2 or 3 as input."
#     exit 1
# fi

# # Check if the input is valid (either 1, 2, or 3)
# if [[ $1 != 1 && $1 != 2 && $1 != 3 ]]; then
#     echo "Invalid input. Please provide either 1, 2, or 3."
#     exit 1
# fi

# current_directory=$(dirname "$0")

# # Clean up previous object files and executable
# rm -f "$current_directory/main.o" "$current_directory/f1.o" "$current_directory/f2.o" "$current_directory/f3.o" "$current_directory/a.out"

# # Compile and link main.c with f1.c
# if [ $1 -eq 1 ]; then
#     gcc -c "$current_directory/main.c" -o "$current_directory/main.o" -DF1_COMPILE
#     gcc -c "$current_directory/f1.c" -o "$current_directory/f1.o"
#     gcc "$current_directory/main.o" "$current_directory/f1.o" -o "$current_directory/a.out"
#     "$current_directory/a.out"
# fi

# # Compile and link main.c with f2.c
# if [ $1 -eq 2 ]; then
#     gcc -c main.c -o main.o -DF2_COMPILE
#     gcc -c f2.c -o f2.o
#     gcc main.o f2.o -o a.out
#     ./a.out
# fi

# # Compile and link main.c with f3.c
# if [ $1 -eq 3 ]; then
#     gcc -c main.c -o main.o -DF3_COMPILE
#     gcc -c f3.c -o f3.o
#     gcc main.o f3.o -o a.out
#     ./a.out
# fi

# # Clean up object files and the final executable
# rm -f main.o f1.o f2.o f3.o a.out