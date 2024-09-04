Title: Greppability is an underrated code metric

URL Source: https://morizbuesing.com/blog/greppability-code-metric/

Markdown Content:
When I’m working on maintaining an unfamiliar codebase, I will spend a lot of time grepping the code base for strings. Even in projects exclusively written by myself, I have to search a lot: function names, error messages, class names, that kind of thing. If I can’t find what I’m looking for, it’ll be frustrating in the best case, or in the worst case lead to dangerous situations where I’ll assume a thing is not needed anymore, since I can’t find any references to it in the code base. From these situations, I’ve derived some rules you can apply to keep your code base greppable:

Don’t split up identifiers
--------------------------

It turns out that splitting up, or dynamically constructing identifiers is a bad idea.

Suppose you have two database tables `shipping_addresses`, `billing_addresses`, it might seem like a perfectly good solution to construct the table name dynamically from the order type.

```
const getTableName = (addressType: 'shipping' | 'billing') => {
    return `${addressType}_addresses`
}
```

Though it looks nice and DRY, it’s not great for maintainenance: someone will inevitably search the code base for the table name `shipping_addresses` and miss this occurence.

Refactored for greppability:

```
const getTableName = (addressType: 'shipping' | 'billing') => {
    if (addressType === 'shipping') {
        return 'shipping_addresses'
    }
    if (addressType === 'billing') {
        return 'billing_addresses'
    }
    throw new TypeError('addressType must be billing or shipping')
}
```

The same goes for column names, object fields, and, god forbid, method/function names (it’s easily possible to dynamically construct method names with javascript).

Use the same names for things across the stack
----------------------------------------------

Don’t rename fields at application boundaries to match naming schemes. An obvious example is then importing postgres-style snake\_case identifiers into javascript, then converting them to camelCase. This makes it harder to find—you now have to grep for two strings instead of one in order to find all occurences!

```
const getAddress = async (id: string) => {
    const address = await getAddressById(id)
    return {
        streetName: address.street_name,
        zipCode: address.zip_code,
    }
}
```

You’re better off biting the bullet and returning the object directly:

```
const getAddress = async (id: string) => {
    return await getAddressById(id)
}
```

Flat is better than nested
--------------------------

Taking inspiration from the [Zen of Python](https://peps.python.org/pep-0020/), when dealing with namespaces, flattening your folders/object structures is mostly better than nesting.

For example if you have two choices to set up your translation files:

```
{
    "auth": {
        "login": {
            "title": "Login",
            "emailLabel": "Email",
            "passwordLabel": "Password",
        },
        "register":
            "title": "Register",
            "emailLabel": "Email",
            "passwordLabel": "Password",
        }
    }
}
```

and

```
{
    "auth.login.title": "Login",
    "auth.login.emailLabel": "Email",
    "auth.login.passwordLabel": "Password",
    "auth.register.title": "Login",
    "auth.register.emailLabel": "Email",
    "auth.register.passwordLabel": "Password",
}
```

take the second option! You will be able to easily find your keys now, which you are probably referring to as something like `t('auth.login.title')`.

Or consider React component structure: a component stucture like

```
./components/AttributeFilterCombobox.tsx
./components/AttributeFilterDialog.tsx
./components/AttributeFilterRating.tsx
./components/AttributeFilterSelect.tsx
```

is preferable to

```
./components/attribute/filter/Combobox.tsx
./components/attribute/filter/Dialog.tsx
./components/attribute/filter/Rating.tsx
./components/attribute/filter/Select.tsx
```

from a greppability perspective, since you’ll be able to grep for the whole namespaced component `AttributeFilterCombobox` just from the usage, as opposed to just `Dialog`, which you might have multiple of accross your application.
