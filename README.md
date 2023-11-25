<div align="center">
<pre>

# scripts
Useful scripts for data entry, data cleansing, etc.
</pre>

## Usage Example

Open a terminal from the directory where the scripts are saved, or open a terminal and navigate to the directory where the scripts are saved.
Type in a string as input, typically a color code followed by some color combination.

### Uppercase

```sh
C:\> python uppercase.py
Your Input>|a100A Some Color/Another Color
```

Hit enter and the output will look like:

```sh
a100A SOME COLOR/ANOTHER COLOR/THIRD COLOR
```

### Lowercase

```sh
C:\> python lowercase.py
Your Input|a100A SOME COLOR/ANOTHER COLOR/THIRD COLOR
```

Hit enter and the output will look like:

```sh
a100A Some Color/Another Color
```

## Meta

Ron Jean-Francois - jeanfrancoisron@gmail.com

## Contributing

1. Fork it (<https://github.com/ronthetech/crow/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
