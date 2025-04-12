Title: Code Review Hot Spots with Semgrep

URL Source: https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/

Markdown Content:
*   [What is a Hot Spot?](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#what-is-a-hot-spot)
*   [Types of Static Analysis Rules](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#types-of-static-analysis-rules)
    *   [Security Rules](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#security-rules)
    *   [Hot Spot Rules](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#hot-spot-rules)
*   [Review of Existing Literature](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#review-of-existing-literature)
    *   [Everyone has a Hot Spot List](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#everyone-has-a-hot-spot-list)
    *   [Hardcoded Secret Detectors](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#hardcoded-secret-detectors)
    *   [The Audit Category in Semgrep Rules](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#the-audit-category-in-semgrep-rules)
        *   [Audit Shouldn't be Under Security in the Semgrep Rules Repository](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#audit-shouldnt-be-under-security-in-the-semgrep-rules-repository)
    *   [Microsoft Application Inspector](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#microsoft-application-inspector)
    *   [weggli by Felix - "Playing with Weggli" by Jonathan & Jordy](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#weggli-by-felix---playing-with-weggli-by-jonathan--jordy)
*   [Different Types of Hot Spots](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#different-types-of-hot-spots)
    *   [1\. Insecure Configurations](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#1-insecure-configurations)
        *   [TLSv1 Support in Go](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#tlsv1-support-in-go)
        *   [Skipping Certificate Verification in Go](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#skipping-certificate-verification-in-go)
        *   [External Entity Injection in Java](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#external-entity-injection-in-java)
        *   [Security Issues in Dockerfiles](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#security-issues-in-dockerfiles)
    *   [2\. Dangerous Functions](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#2-dangerous-functions)
        *   [MD5](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#md5)
        *   [sizeof(\*ptr) in C](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#sizeofptr-in-c)
        *   [text/template in Go](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#texttemplate-in-go)
        *   [Unsafe in Go](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#unsafe-in-go)
    *   [3\. Dangerous Patterns](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#3-dangerous-patterns)
        *   [Formatted SQL Strings in Java](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#formatted-sql-strings-in-java)
        *   [Return Value of openssl\_decrypt in PHP](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#return-value-of-openssl_decrypt-in-php)
        *   [Hardcoded Secrets](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#hardcoded-secrets)
    *   [4\. Interesting Keywords](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#4-interesting-keywords)
        *   [Function with Encode and Decode in Their Names](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#function-with-encode-and-decode-in-their-names)
        *   [Bug and Feature Tracking Codes](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#bug-and-feature-tracking-codes)
*   [How Do I Collect These?](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#how-do-i-collect-these)
    *   [1\. Static Analysis Rules](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#1-static-analysis-rules)
    *   [2\. Coding Standards](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#2-coding-standards)
    *   [3\. Documentation](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#3-documentation)
    *   [4\. Other Bugs](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#4-other-bugs)
    *   [5\. Experience](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#5-experience)
*   [What Did We Learn Here Today?](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#what-did-we-learn-here-today)

I will discuss the (not novel) concept of code review hot spots. Hot spots are parts of the code that might contain vulnerabilities. They are not suitable for automatic reporting, so security engineers should review them manually. I will define what I call a hot spot; I'll find some examples with Semgrep; and finally, I'll show how I collect these rules.

What is a Hot Spot?[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#what-is-a-hot-spot)
-----------------------------------------------------------------------------------------------------------------

In this context, hot spots are parts of code that _might_ contain security vulnerabilities. You are not "always" looking for a specific problem, but rather bad practices, common mistakes, insecure configurations, and in short, places where bad things usually happen.

It's impossible to review every line of code in a modern software project. So we search for a mental or written list of keywords like `SSLv3`, `MD5`, `memcpy`, or `encrypt/decrypt`. We are not sure we'll find anything, but these are good places to start looking for bugs.

Types of Static Analysis Rules[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#types-of-static-analysis-rules)
--------------------------------------------------------------------------------------------------------------------------------

You (as a security engineer) should have two separate groups of security-focused static analysis rules:

1.  `security`: For developers.
2.  `hotspots`: For security engineers.

Security Rules[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#security-rules)
--------------------------------------------------------------------------------------------------------

`security` rules detect specific vulnerabilities (e.g., `log4j`). Ideally, they should be lightweight and return zero false positives. I should enable the developers to deploy my rules in their workflow (e.g., CI/CD pipeline or editor) with confidence and have faith that I will not waste their time. If not, they will stop trusting me and throw away (or circumvent) the application security apparatus. I would do the same.

Hot Spot Rules[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#hot-spot-rules)
--------------------------------------------------------------------------------------------------------

`hotspots` are for me. I want to find error-prone parts of the code. I can usually discard false positives with a quick review. These rules should be very noisy, but don't spend too much time reducing the noise.

Review of Existing Literature[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#review-of-existing-literature)
--------------------------------------------------------------------------------------------------------------------------------

I am not proposing a novel idea. I have learned from others.

Everyone has a Hot Spot List[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#everyone-has-a-hot-spot-list)
--------------------------------------------------------------------------------------------------------------------------------

Every security engineer has a personal (mental or written) list of keywords accumulated over time. [.NET Interesting Keywords to Find Deserialization Issues](https://gist.github.com/irsdl/9315521bab79fe972859874b5f2185af) by [irsdl](https://twitter.com/irsdl) is a good example. You can find similar lists with a quick search. Collecting these are fun.

Hardcoded Secret Detectors[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#hardcoded-secret-detectors)
--------------------------------------------------------------------------------------------------------------------------------

Hardcoded secrets are hot spots. There are a gazillion products and regular expressions to find API keys, passwords, and encryption keys. The results usually have high false positives and require manual review.

The Audit Category in Semgrep Rules[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#the-audit-category-in-semgrep-rules)
--------------------------------------------------------------------------------------------------------------------------------

The [Semgrep rules](https://github.com/returntocorp/semgrep-rules#rule-namespacing) repository stores calls them `audit` rules and stores them under `security/audit`. You can run them all with the [p/security-audit](https://semgrep.dev/p/security-audit) policy.

> If a security rule is discouraging the use of a bad pattern (such as formatted SQL strings), we recommend appending audit to your namespace. This distinguishes it from a security rule that is specifically aiming to detect a vulnerability.

### Audit Shouldn't be Under Security in the Semgrep Rules Repository[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#audit-shouldnt-be-under-security-in-the-semgrep-rules-repository)

**Semgrep bashing ahead.**

> Et tu, Parsia?

TL;DR: Running rules under `security` will also run the noisier `audit`. `security` and `audit` should be separate categories in my opinion. You can avoid this issue by using policies but it's still a problem with local rules.

Semgrep can use local rules with `--config /path/to/rules/`. It will run every rule in the path and any subdirectories. So, `--config semgrep-rules/python/lang/security` will also run the rules in `python/lang/security/audit`

We can directly use the registry without downloading the rules. `--config r/python.lang.security` will run all the rules in the registry under `/python/lang/security` including `audit`.

This behavior is not ideal. `audit` rules are noisy by design. I have organized our internal Semgrep rules differently. E.g., we have `python.lang.security` and `python.lang.hotspots`. I can pass the rules in `security` to developers and keep the noisy `hotspots` for ourselves.

Microsoft Application Inspector[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#microsoft-application-inspector)
--------------------------------------------------------------------------------------------------------------------------------

[Microsoft Application Inspector](https://github.com/microsoft/ApplicationInspector) is a "what's in the code" tool. It has built-in features like `cryptography` or `authentication`. Each rule belongs to a feature and contains a list of keywords/regular expressions. If a rule has a hit, the final report will include that feature. For example, if the code has `md5` the application has the `cryptography`.

I played with Application Inspector and [DevSkim](https://github.com/microsoft/DevSkim) (an IDE linter that uses the same rule format) for a few weeks but decided they were not for me. Application Inspector is designed to present features (e.g., this app has `authentication`), but I was interested in navigating and reviewing the results.

weggli by Felix - "Playing with Weggli" by Jonathan & Jordy[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#weggli-by-felix---playing-with-weggli-by-jonathan--jordy)
--------------------------------------------------------------------------------------------------------------------------------

A few days ago, I was looking at some C++ rules in [weggli](https://github.com/googleprojectzero/weggli). `weggli` is a C/C++ static analysis tool by [Felix Wilhelm](https://twitter.com/_fel1x) from Google Project Zero. weglli and Semgrep use the same parser ([Tree-Sitter](https://tree-sitter.github.io/tree-sitter/)) and have similar rule patterns. The readme has a list of examples and I ported some to Semgrep.

I also found [Playing with Weggli](https://dustri.org/b/playing-with-weggli.html) by Julien Voisin and [Jordy (Oblivion)](https://pwning.systems/about/). They ran some custom weggli rules on the Linux codebase. The blog gave me ideas for Semgrep rules (see the `sizeof(*ptr)` rule discussed later).

Thanks, Felix, Jonathan, and Jordy!

Different Types of Hot Spots[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#different-types-of-hot-spots)
--------------------------------------------------------------------------------------------------------------------------------

I have created a simple category for hot spots. I will define each one and discuss examples.

1.  **Insecure Configurations**: A (usually 3rd party) component with a vulnerable configuration.
2.  **Dangerous Functions**: Using these functions is usually a security problem.
3.  **Dangerous Patterns**: Safe methods and constructs that are used insecurely.
4.  **Interesting Keywords**: Specific terms in variable/class/method names and comments.

1\. Insecure Configurations[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#1-insecure-configurations)
--------------------------------------------------------------------------------------------------------------------------------

**The framework, library, or infrastructure's configuration is insecure.** We can usually find insecure configurations by the existence (or omission) of certain reserved keywords. These configurations can be in the code or config files (d'oh).

### TLSv1 Support in Go[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#tlsv1-support-in-go)

Look for [VersionTLS10](https://github.com/golang/go/blob/01c83be7932e7f51333c813460752f09f78ec2c4/src/crypto/tls/common.go#L29) and `VersionSSL30`[1](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#fn:1) in Go code to see support for TLSv1.0 or SSLv3. Use this simple Semgrep rule ([https://semgrep.dev/s/parsiya:blog-2022-03-go-tlsv1](https://semgrep.dev/s/parsiya:blog-2022-03-go-tlsv1)) to find these hot spots and even automagically [fix them](https://parsiya.net/blog/2021-10-25-a-hands-on-intro-to-semgreps-autofix/ "fix them").

![Image 1: Detecting TLSv1 support with Semgrep](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/01-tlsv1.png) Detecting TLSv1 support with Semgrep

There's a similar rule in the Semgrep registry: [https://semgrep.dev/r?q=go-stdlib.disallow-old-tls-versions](https://semgrep.dev/r?q=go-stdlib.disallow-old-tls-versions).

### Skipping Certificate Verification in Go[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#skipping-certificate-verification-in-go)

We can disable TLS certificate[2](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#fn:2) checks in Go with [InsecureSkipVerify](https://github.com/golang/go/blob/01c83be7932e7f51333c813460752f09f78ec2c4/src/crypto/tls/common.go#L641). It's bad, but not necessarily a problem. We might be dealing with internal endpoints without valid certificates[3](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#fn:3).

If `InsecureSkipVerify` is true, we can use the optional [VerifyPeerCertificate](https://github.com/golang/go/blob/01c83be7932e7f51333c813460752f09f78ec2c4/src/crypto/tls/common.go#L590) callback to do our own checks. The last stand is [VerifyConnection](https://github.com/golang/go/blob/01c83be7932e7f51333c813460752f09f78ec2c4/src/crypto/tls/common.go#L603) which is executed for all connections and can terminate the TLS handshake.

Another simple Semgrep rule to find all three keywords: [https://semgrep.dev/s/parsiya:blog-2022-03-go-cert-check](https://semgrep.dev/s/parsiya:blog-2022-03-go-cert-check).

![Image 2: Go certificate bypass check](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/02-go-cert.png) Go certificate bypass check

The rule in the Semgrep registry at [https://semgrep.dev/r?q=go-stdlib.bypass-tls-verification](https://semgrep.dev/r?q=go-stdlib.bypass-tls-verification) takes advantage of the Sem(antic) in Semgrep and looks for things like `tls.Config{..., InsecureSkipVerify: true, ...}`.

### External Entity Injection in Java[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#external-entity-injection-in-java)

Java is notorious for [External Entity Injection (XXE) problems](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html#java). Most XML parsing libraries do not have secure defaults. We use hardcoded strings and language constants to look for them. For example, `DocumentBuilderFactory`.

The existing Semgrep rules do a decent job of eliminating false positives, but it's impossible to find everything. A hot spot rule has an easier time and can flag all of them for manual review. I used the [OWASP XML External Entity Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html#java) to compose a list (warning: lots of noise): [https://semgrep.dev/s/parsiya:blog-2022-03-java-xxe](https://semgrep.dev/s/parsiya:blog-2022-03-java-xxe).

![Image 3: Java XXE Hail Mary](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/05-java-xxe-hail-mary.png) Java XXE Hail Mary

### Security Issues in Dockerfiles[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#security-issues-in-dockerfiles)

dockerfiles are essentially configuration files. Containers are versatile. We can shoot ourselves in the foot (lookout C++! a new contender is here). Our hot spot rules can look for things like [is it running as root?](https://semgrep.dev/r?q=docker+last-user-is-root) or [source is not pinned](https://semgrep.dev/r?q=dockerfile-source-not-pinned).

**Almost all cloud, k8s, and similar configuration issues fall into this category.** Find how a configuration can be insecure, add their respective keywords to your rules and run them on everything.

2\. Dangerous Functions[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#2-dangerous-functions)
------------------------------------------------------------------------------------------------------------------------

**Every programming language, framework, and library has dangerous functions.** However, their existence is not necessarily a vulnerability. You could say that we should not use these dangerous functions and I agree, but removing them is not always practical, especially in legacy code.

### MD5[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#md5)

`MD5` is a cryptographically broken hash function (emphasis on "cryptographically"). That said, we cannot report every instance. There are cases where using `MD5` is completely fine. I have seen some safe examples in the real world:

1.  A custom content management system (e.g., a blog) used MD5 to create an identifier for images. If you can edit the blog post and add a different image with the same hash, you can do bad things and overwrite the previous one. This is useless because you can just delete the original image with your access.
2.  Generating a database index from a 20 digit numerical user ID. The ID has to be a valid number. As far as I know, it's impossible to generate an MD5 collision with two numbers (ready to be proven wrong).

Flagging `MD5` is the knee-jerk reaction. Maybe you will create a ticket and ask the developers to change it to SHA-256 "to be sure." Keep in mind that your reputation will take a hit by asking developers to spend cycles without a plausible vulnerability.

The "insecure randoms" like `java.lang.Math.random` are similar. They are OK to use in a non-cryptographic context. A ticket about the "tip of the day" module not using a CSPRNG (Cryptographically Secure PseudoRandom Number Generator) is silly.

### sizeof(\*ptr) in C[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#sizeofptr-in-c)

Using `sizeof(pointer)` instead of the actual object type is a common mistake in C/C++. In this example we are using `memcpy(dst, src, sizeof(char*))` which results in a classic buffer overflow. `sizeof(char*)` is usually 4 (x86) or 8 (x64) bytes while the `sizeof(char)` is 1.

```
#include <stdio.h>
#include <string.h>

int main() {

  char dst[20];
  char* src = "hello hello";

  // seg fault - sizeof(char*) == 8
  memcpy(dst, src, strlen(src)*sizeof(char*));

  // sizeof(char): 1 - sizeof(char*): 8 - sizeof(source): 8
  // printf("sizeof(char): %lu - sizeof(char*): %lu - sizeof(src): %lu\n",
  //    sizeof(char), sizeof(char*), sizeof(src));
}
```

Interestingly, with`memcpy(dst, src, sizeof(src))` we get a warning:

```
warning: 'memcpy' call operates on objects of type 'char' while the size is
based on a different type 'char *'
[-Wsizeof-pointer-memaccess]
  memcpy(dst, src, sizeof(src));
```

I created a rule to find all `sizeof($TYPE*)` in the code with `pattern-regex`. This will also search comments. We can reduce the false positives with `pattern-not-regex`. Try extending [https://semgrep.dev/s/parsiya:blog-2022-03-sizeof-ptr](https://semgrep.dev/s/parsiya:blog-2022-03-sizeof-ptr).

![Image 4: sizeof(pointer) Semgrep rule](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/03-sizeof.png) sizeof(pointer) Semgrep rule

It's also possible to ditch regex and just use a pattern like this:

```
rules:
- id: blog-2022-03-sizeof-ptr
  pattern: sizeof($OBJ*)
  message: Using sizeof($OBJ*) is wrong, did you mean sizeof($OBJ)?
  languages:
    - c
    - cpp
  severity: WARNING
```

### text/template in Go[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#texttemplate-in-go)

Go's standard library offers two template packages. [html/template](https://pkg.go.dev/html/template) does some output encoding while [text/template](https://pkg.go.dev/text/template) does none. Using `text/template` in a web application might lead to XSS. We should review find and review `text/template` imports.

The Semgrep registry has an [audit rule](https://semgrep.dev/r?q=text-template) for this problem. I am recycling my similar rule from the [autofix blog](https://parsiya.net/blog/2021-10-25-a-hands-on-intro-to-semgreps-autofix/#go---texttemplate "autofix blog"): [https://semgrep.dev/s/parsiya:go-import-text-template-fix](https://semgrep.dev/s/parsiya:go-import-text-template-fix).

### Unsafe in Go[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#unsafe-in-go)

My attempt at an unoriginal programming language joke:

> Under the standard library of every secure programming language are a bunch of unsafes.

Go and Rust are considered secure programming languages, but both allow us to use `unsafe` via [Go's unsafe package](https://pkg.go.dev/unsafe) and [Rust's unsafe keyword](https://doc.rust-lang.org/std/keyword.unsafe.html).

Should we flag all unsafes? Depends on the industry. I don't. Game devs love to use clever hacks. Finding these instances are easy. Look for `import "unsafe"` in Go and `unsafe` in Rust. A sample rule for Go (Semgrep doesn't support Rust, but Rust is already secure :p): [https://semgrep.dev/s/parsiya:blog-2022-03-go-unsafe](https://semgrep.dev/s/parsiya:blog-2022-03-go-unsafe).

![Image 5: Finding unsafe imports in Go](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/06-go-unsafe.png) Finding unsafe imports in Go

3\. Dangerous Patterns[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#3-dangerous-patterns)
----------------------------------------------------------------------------------------------------------------------

**Dangerous patterns often lead to security vulnerabilities.** Think of them as "insecure usage of usually safe methods."

### Formatted SQL Strings in Java[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#formatted-sql-strings-in-java)

The Semgrep registry has [a rule](https://semgrep.dev/playground?registry=java.lang.security.audit.formatted-sql-string.formatted-sql-string) that looks intimidating but is just trying to find concatenated strings executed as SQL queries.

![Image 6: SQL query caught by this rule](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/04-sql-string.png) SQL query caught by this rule

If you have time, flag and review every SQL query. `exec` (and similar) commands are also good choices. We want to review them and check if an attacker can influence their input and get command injection.

### Return Value of openssl\_decrypt in PHP[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#return-value-of-openssl_decrypt-in-php)

I encountered this problem recently. The [openssl\_decrypt](https://www.php.net/manual/en/function.openssl-decrypt.php) is a safe function in PHP returns the decrypted string on success, but `false` on failure. We might have a vulnerability if we don't check this edge case. The [openssl-decrypt-validate](https://semgrep.dev/playground?registry=php.lang.security.audit.openssl-decrypt-validate.openssl-decrypt-validate) Semgrep rule flags these cases for review:

### Hardcoded Secrets[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#hardcoded-secrets)

Let's say you are storing the AES keys in the source code or in a config file. This is a dangerous pattern. AES is secure and not a dangerous function but you have weakened it because everyone with access to the code is now able to break your encryption.

Using a static salt in your password hashing scheme is the same. You have weakened your (hopefully) secure algorithm.

4\. Interesting Keywords[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#4-interesting-keywords)
--------------------------------------------------------------------------------------------------------------------------

**Look for specific variable/method/class names, and comments**. These are not language keywords but rather contextual concepts (wut?!).

Have you ever searched for `password` in a codebase to discover how passwords are handled? They are probably stored in variables named `password`, `passwrd`, or another variation. What about searching for `TODO` or `security` in the code comments?

### Function with Encode and Decode in Their Names[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#function-with-encode-and-decode-in-their-names)

[weggli](https://github.com/googleprojectzero/weggli) has an example to find functions with `decode` in their names. I want to review any function that has `encode` and `decode` in its name. `encrypt/decrypt` is another good choice. These functions probably increase our attack surface because we are dealing with two different formats. Parser bugs are fun!

The Semgrep rule at [https://semgrep.dev/s/parsiya:blog-2022-03-encode-decode-function-name](https://semgrep.dev/s/parsiya:blog-2022-03-encode-decode-function-name) was easy to create (man, I love Semgrep). We capture all functions in a metavariable `$FUNC(...)`, then use `metavariable-regex` to filter them.

![Image 7: Find functions with encode/decode in their name](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/07-encode-decode.png) Find functions with encode/decode in their name

### Bug and Feature Tracking Codes[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#bug-and-feature-tracking-codes)

Bugs are usually mentioned in code comments. For example, if I fix the ticket `BUG-1234` I add a comment to that location in the code with some other information. The same for new features or merge/pull requests. Search for these patterns in code to find features, fixed bugs, existing bugs, **workarounds** (`// BUG-234: hacky way of bypassing a security guardrail!`), and other interesting things.

During my lucky [RCE in the WSL Remote extension](https://parsiya.net/blog/2021-12-20-rce-in-visual-studio-codes-remote-wsl-for-fun-and-negative-profit/ "RCE in the WSL Remote extension") I found a reference to a CVE in the [VS Code server code](https://github.com/microsoft/vscode/blob/48b6c6a5ffca58a3fd7dc281419c42f8f9abc35a/src/vs/server/node/remoteExtensionHostAgentServer.ts#L677).

The page for [CVE-2021-1416](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2020-1416) doesn't have much information. The code tells a much better story. VS Code server would loads code from `node_modules` in specific paths on Windows. If an attacker could put their own Node modules in those paths, they could achieve RCE. Why is `Azure Storage Explorer` even running this code?!

![Image 8: CVE-2020-1416 in code](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/09-cve.png) CVE-2020-1416 in code

We can search for items like `CVE*`, `BUG-[number]`, and `CL[number]` (CL stands for `Change List` in perforce which is the equivalent of a git commit).

How Do I Collect These?[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#how-do-i-collect-these)
-------------------------------------------------------------------------------------------------------------------------

I have already explained where my examples have come from. Let's make a list:

1.  Static analysis rules
2.  Coding standards
3.  Documentation
4.  Other bugs
5.  Experience

1\. Static Analysis Rules[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#1-static-analysis-rules)
----------------------------------------------------------------------------------------------------------------------------

Go through static analysis rules for different languages and tools. I went through Semgrep's `audit` rules and weggli examples. Check out [GitHub Security Lab's CodeQL queries](https://github.com/github/securitylab/tree/main/CodeQL_Queries) for more. While it's impossible to replicate some of CodeQL rules in Semgrep, extract keywords for manual review.

Why Semgrep and not CodeQL then? The short answer is [CodeQL is nice but doesn't work for me](https://parsiya.net/blog/2021-06-22-semgrep-the-surgical-static-analysis-tool/ "CodeQL is nice but doesn't work for me").

You can even use patterns from other languages and adapt them to your target. We just saw XXE in Java, but it also happens in other languages. Search for `xml + other-language` and see what you can find.

The keywords in [Microsoft Application Inspector](https://github.com/microsoft/ApplicationInspector) and [DevSkim](https://github.com/microsoft/DevSkim) rules are useful.

2\. Coding Standards[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#2-coding-standards)
------------------------------------------------------------------------------------------------------------------

Programming languages and development teams usually have their own coding standards. Some functions and libraries are banned; some patterns are actively discouraged. Add these to your list.

You can find legacy code, one-time exceptions ("hey can I use memcpy here once?"), and items missed in code reviews.

3\. Documentation[](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/#3-documentation)
------------------------------------------------------------------------------------------------------------

Reading and writing documentation is a great way to learn.

Sometimes the **programming language** has warnings in `in large, friendly letters`.

![Image 9: Don't Panic! credit: nclm, CC0, via Wikimedia Commons](https://parsiya.net/blog/2022-04-07-code-review-hot-spots-with-semgrep/08-dont-panic.png) Don't Panic! credit: nclm, CC0, via Wikimedia Commons

A good example (thanks to my friend [Tim Michaud](https://twitter.com/TimGMichaud)) is PHP's [unserialize](ht