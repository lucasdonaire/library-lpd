a = [1 2 3; 4 5 6];
b = [1 2];
x = a\b';
disp(x)
disp(a*x)

function res = solveLinear(A,b)
return A\b
endfunction
