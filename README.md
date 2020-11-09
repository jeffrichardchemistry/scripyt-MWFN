# scripyt-MWFN
Script to scrap CP properties of multiwfn output

# Install via setuptools

```
$ git clone https://github.com/jeffrichardchemistry/scripyt-MWFN
$ cd scripyt-MWFN
$ python3 setup.py install
```

# Install via pip

```
$ pip install scripyt-MWFN
```

# Run script
<b>Parameters:</b>
<ul>
  <li><b>-p:</b> Path to Multiwfn output file</li>
  <li><b>-cp:</b> CPs desired to extract the information</li>
</ul>

```
$ scripyt-MWFN -p path/to/Multiwfn_output_file -cp 1 2 3 4 5 6
```

Saving terminal output into a file:

```
$ scripyt-MWFN -p path/to/Multiwfn_output_file -cp 1 2 3 4 5 6 > log.txt
```
