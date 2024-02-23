#!/usr/bin/env python3

# Author: caleb7023

SineCalcMemo   = []
CosineCalcMemo = []

SineCalcMaxTerms   = 1
CosineCalcMaxTerms = 1

SineCalcMemoSign   = 1
CosineCalcMemoSign = 1

SineCalcSimpleFactorialMemo   = 1
CosineCalcSimpleFactorialMemo = 1

PI = 3.14159265366



def Sin(Theta, Terms: int=8, modulo: bool=True):

    """
    # Sin

    ## How is it calculated

    $ \sin \theta $ will be cauclated using the formula below:

    $$ \sin \theta = \sum_{n=1}^{\infin}{\frac{(-1)^n}{(2n+1)!}}θ^{2n+1}
    """
    # Maybe its easier to display like thin in the code
    # sin(x) = sum(((-1) ^ n / (2n + 1)!) * x ^ (2n + 1))

    # If modulo was true, this will prevent the function fuckin up when the Theta isnt in the range of -π to π
    if modulo:
        if -PI < Theta < PI:
            Input = Theta - PI % PI + PI # TODO: Make the code more efficient ig
        else:
            Input = Theta
    else:
        Input = Theta

    global SineCalcMaxTerms, SineCalcMemoSign, SineCalcSimpleFactorialMemo, SineCalcMemo

    # This gonna memo the (-1) ^ n / (2n + 1)! part if the Terms value was higher than last maximum terms
    # This makes the process fast asf cus its gonna list all the calc and be desired when its needed
    if SineCalcMaxTerms < Terms:

        for i in range(SineCalcMaxTerms, Terms):
            
            # Invert the sign
            SineCalcMemoSign *= -1

            # Factorial
            SineCalcSimpleFactorialMemo *= 2 * i
            SineCalcSimpleFactorialMemo *= 2 * i + 1

            # Memo the calc result of (-1) ^ n / (2n + 1)!
            SineCalcMemo += [SineCalcMemoSign / SineCalcSimpleFactorialMemo]
        
        SineCalcMaxTerms = Terms
    
    Ans = Input

    SineCalcPowerMemo = Input

    # Sum: sum(((-1) ^ n / (2n + 1)!) * x ^ (2n + 1))
    for i in range(1, Terms):

        # Power
        SineCalcPowerMemo *= Input
        SineCalcPowerMemo *= Input

        # Sum add
        Ans += SineCalcMemo[i-1] * SineCalcPowerMemo

    return Ans



def Cos(Theta, Terms: int=8, modulo: bool=True):

    """
    # Cos

    ## How is it calculated

    $ \cos \theta $ will be cauclated using the formula below:

    $$ \cos \theta = \sum_{n=1}^{\infin}{\frac{(-1)^n}{(2n)!}}θ^{2n}
    """
    # Maybe its easier to display like thin in the code
    # cos(x) = sum(((-1) ^ n / 2n!) * x ^ 2n)

    # If modulo was true, this will prevent the function fuckin up when the Theta isnt in the range of -π to π
    if modulo:
        if -PI < Theta < PI:
            Input = Theta - PI % PI + PI # TODO: Make the code more efficient ig
        else:
            Input = Theta
    else:
        Input = Theta

    global CosineCalcMaxTerms, CosineCalcMemoSign, CosineCalcSimpleFactorialMemo, CosineCalcMemo

    # This gonna memo the (-1) ^ n / 2n! part if the Terms value was higher than last maximum terms
    # This makes the process fast asf cus its gonna list all the calc and be desired when its needed
    if CosineCalcMaxTerms < Terms:

        for i in range(CosineCalcMaxTerms, Terms):

            # Invert the sign
            CosineCalcMemoSign *= -1

            # Factorial
            CosineCalcSimpleFactorialMemo *= 2 * i - 1
            CosineCalcSimpleFactorialMemo *= 2 * i

            # Memo the calc result of (-1) ^ n / 2n!
            CosineCalcMemo += [CosineCalcMemoSign / CosineCalcSimpleFactorialMemo]
        
        CosineCalcMaxTerms = Terms
    
    Ans = 1

    SineCalcPowerMemo = Input

    # Sum: sum(((-1) ^ n / 2n!) * x ^ 2n)
    for i in range(1, Terms):

        # Power
        SineCalcPowerMemo *= Input
        SineCalcPowerMemo *= Input

        # Sum add
        Ans += CosineCalcMemo[i-1] * SineCalcPowerMemo

    return Ans



def Tan(Theta, Terms: int=8, modulo: bool=True):

    """
    # Tan

    ## How is it calculated

    $ \tan \theta $ will be cauclated using the formula below:

    $$ \tan \theta = \frac{\sin \theta}{\cos \theta}
    """
    # Maybe its easier to display like thin in the code
    # tan(x) = sin(x) / cos(x)

    # If modulo was true, this will prevent the function fuckin up when the Theta isnt in the range of -π to π
    if modulo:
        if -PI < Theta < PI:
            Input = Theta - PI % PI + PI # TODO: Make the code more efficient ig
        else:
            Input = Theta
    else:
        Input = Theta

    return Sin(Input, Terms, False) / Cos(Input, Terms, False) # ez