# code

```
echo "# code" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/garnetsoft/code.git
git push -u origin master
```

# coding practice 

1. Standardizing code formatting

2. Don't follow the DRY (Don't Repeat Yourself) principle blindly

3. Debug code via logs

4. Beware of premature optizations 

5. Don't complicate your codebase with unnecessary features

6. Setup a CI/CD pipeline early in the development lifecycle

# Construct a mask of which columns are numeric
numeric_col_mask = df.dtypes.apply(lambda d: issubclass(np.dtype(d).type, np.number))

# Dict used to center the table headers
d = dict(selector="th",
    props=[('text-align', 'center')])

# Style
df.style.set_properties(subset=df.columns[numeric_col_mask], # right-align the numeric columns and set their width
                        **{'width':'10em', 'text-align':'right'})\
        .set_properties(subset=df.columns[~numeric_col_mask], # left-align the non-numeric columns and set their width
                        **{'width':'10em', 'text-align':'left'})\
        .format(lambda x: '{:,.0f}'.format(x) if x > 1e3 else '{:,.2f}'.format(x), # format the numeric values
                subset=pd.IndexSlice[:,df.columns[numeric_col_mask]])\
        .set_table_styles([d]) # center the header
