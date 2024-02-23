# Trigonometric functions

This is a repo that saves the code of the hmath's TrigonometricFunctions.

## Sin

### How is it calculated

$` \sin \theta `$ will be cauclated using the formula below:

$$ \sin \theta = \sum_{n=1}^{\infty}{\frac{(-1)^n}{(2n+1)!}}θ^{2n+1} $$

### Inputs

`Theta` : Sin(x)'s x

`Terms` : Accuracy. Only int numbers are allowed. [defult=8]

`Modulo`: Will modulo the theta when calc or not. Only False or True is allowed. [defult=True]

## Cos

### How is it calculated

$` \cos \theta `$ will be cauclated using the formula below:

$$ \cos \theta = \sum_{n=1}^{\infty}{\frac{(-1)^n}{2n!}}θ^{2n} $$

### Inputs

`Theta` : Cos(x)'s x

`Terms` : Accuracy. Only int numbers are allowed. [defult=8]

`Modulo`: Will modulo the theta when calc or not. Only False or True is allowed. [defult=True]


## Tan

### How is it calculated

$` \tan \theta `$ will be cauclated using the formula below:

$$ \tan \theta = \frac{\sin \theta}{\cos \theta} $$

### Inputs

`Theta` : Tan(x)'s x

`Terms` : Accuracy. Only int numbers are allowed. [defult=8]

`Modulo`: Will modulo the theta when calc or not. Only False or True is allowed. [defult=True]
