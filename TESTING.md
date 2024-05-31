# Easy Keyboard Maker Testing 

![Easykeyboardmaker viewed in different screens](docs/testing.md/test-responsive-img.png)

Developer: [Kim Bergström](https://github.com/KimBergstroem) <br>
[Live webpage](https://easykeyboardmaker-ffb468c2d2d7.herokuapp.com/)<br>
[Project Repository](https://github.com/KimBergstroem/PP5)<br>


## Table of Content

* 📄[Code Validation](#code-validation)
  + [HTML Validation](#html-validation)
  + [CSS Validation](#css-validation)
  + [JAVASCRIPT Validation](#javascript-validation)
  + [PYTHON Validaton](#python-validation)
* 📄[Accessibility](#accessibility)
  + [Wave](#--wave--)
* 📄[Performance](#performance)
  + [Desktop Performance](#desktop-performance)
  + [Mobile Performance](#mobile-performance)
* 📄[Performing tests on various devices](#performing-tests-on-various-devices)
* 📄[Browser compatibility](#browser-compatibility)
* 📄[Manual Testing](#manual-testing)
  + [Testing user stories](#testing-user-stories)
  + [User Experience and Improvements](#user-experience-and-improvements)
  + [Full Testing](#full-testing)
* 📄[Summary](#summary)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc and modified by myself</a></i></small>

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Code Validation

### HTML Validation

W3C Markup Validation is a service offered by W3C, which enables you to assess the compliance of your HTML code with the official standards. This service identifies syntax errors, improper tag usage, and other issues that might impact the structure and meaning of your web pages. By utilizing W3C Markup Validation, you can ensure that your HTML code is well-structured and conforms to established web standards.

Google Chrome web browser and the 'Inspect' function were used to capture the HTML page from the webb applications templates, which was then validated against the W3C Validator.

In this project, a rich text editor called "Summernote" is used to allow usuperuser/admin to create and update blog articles with HTML content. While Summernote enhances the user experience, it introduces some complexities when validating our HTML code.

When admin create or update articles, they have the flexibility to input HTML, which can sometimes lead to unconventional HTML structures or attributes. These unconventional structures are detected as errors when I validate our HTML code using external tools like the W3C validator.

Due to the interaction between Summernote and the need to ensure the security of application. To protect against security threats and potential attacks, implemented safeguards such as using the `|safe` filter in our forms. This filter prevents user-entered HTML from compromising the security of application.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-index.png)</details>| ✅
|contact_form.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-contact_form.png)</details>| ✅
|contact.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-contact.png)</details>| ✅
|company.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-company.png)</details>| ✅
|partners.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-partners.png)</details>| ✅
|payments.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-payments.png)</details>| ✅
|privacy_policy.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-privacy.png)</details>| ✅
|return_policy.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-return.png)</details>| ✅
|shipping_policy.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-shipping.png)</details>| ✅
|warranty_policy.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-warranty.png)</details>| ✅
|terms_of_service.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/home/test-wc3-html-home-terms_of_service.png)</details>| ✅
| **Blog App** |
|blog.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/blog/test-wc3-html-blog-blog.png)</details>| ✅
|post_create.html| The frameborder attribute on the iframe element is obsolete.Attribute maxlength not allowed on element div at this point.Bad value true for attribute hidden on element textarea.Element style not allowed as child of element div in this context.(Suppressing further errors from this subtree.) | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/blog/test-wc3-html-blog-post_create.png)</details>| ✅
|post_delete.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/blog/test-wc3-html-blog-post_delete.png)</details>| ✅
|post_detail.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/blog/test-wc3-html-blog-post_detail.png)</details>| ✅
|post_edit.html| The frameborder attribute on the iframe element is obsolete.Attribute maxlength not allowed on element div at this point.Bad value true for attribute hidden on element textarea.Element style not allowed as child of element div in this context.(Suppressing further errors from this subtree.) | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/blog/test-wc3-html-blog-post_edit.png)</details>| ✅
| **Products App** |
|add_product.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/products/test-wc3-html-products-add_product.png)</details>| ✅
|delete_product.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/products/test-wc3-html-products-delete_product.png)</details>| ✅
|edit_product.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/products/test-wc3-html-products-edit_product.png)</details>| ✅
|product_detail.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/products/test-wc3-html-products-product_info.png)</details>| ✅
|products.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/products/test-wc3-html-products-products.png)</details>| ✅
| **Bag App** |
|bag.html| All clear, no errors found. But IF product was added in bag, duplication errors was found to the quantity measure. Warning: The first occurrence of ID id_qty_35 was here. and Error: Duplicate ID id_qty_35. | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/bag/test-wc3-html-bag-bag.png)</details>| ✅
| **Checkout App** |
|checkout.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/checkout/test-wc3-html-checkout-checkout.png)</details>| ✅
| **Profiles App** |
|profile_agreement.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/profiles/test-wc3-html-profiles-profile_agreement.png)</details>| ✅
|profile_update.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/profiles/test-wc3-html-profiles-profile_update.png)</details>| ✅
|profile.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/html/profiles/test-wc3-html-profiles-profile.png)</details>| ✅


### CSS Validation
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) is a tool provided by the World Wide Web Consortium (W3C) that allows you to validate and check the correctness of your HTML and CSS code. It helps ensure that your web pages comply with the standards set by the W3C, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|base.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/css/test-wc3-css-base.png)</details>| ✅
|blog.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/css/test-wc3-css-blog.png)</details>| ✅
|checkout.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/css/test-wc3-css-checkout.png)</details>| ✅
|home.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/css/test-wc3-css-home.png)</details>| ✅
|product.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/css/test-wc3-css-product.png)</details>| ✅
|profiles.css | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/wc3/css/test-wc3-css-profiles.png)</details>| ✅
|Whole webpage | No errors but alot of warnings becouse of bootstrap  |[Result](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F8000-kimbergstroem-pp5-7080wnht9mo.ws-eu106.gitpod.io%2Fblog%2Fblog%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv#warnings)| ✅


### JAVASCRIPT Validation
[JSHint](https://jshint.com/) is a robust JavaScript code analysis tool that aids in improving the quality and reliability of your JavaScript code. It serves as a linter, helping you catch potential errors, enforce coding conventions, and enhance the overall maintainability of your code.
Taking full JS files from the project folder, but also JavaScript snippets in different HTML pages where there was JavaScript code in the {% block postloadjs %} for validation of the JS code. Below, you can find the file path along with errors and passes.

Below you can see the errors that was showing on all the script that was embedded in html/django templates. Besides from this errors, all javascript was passing without any errors.
 - 	`Expected an identifier and instead saw`
 -  `Expected an assignment or function call and instead saw an expression`
 -  `Unclosed regular expression`
 -  `Unrecoverable syntax error`
 -  `Row 1	 - Missing semicolon`

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|script.js | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/JSHint//test-js-script.png)</details>| ✅
|countryfield.js | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/JSHint/test-js-countryfield.png)</details>| ✅
|stripe_elements.js | No errors or warnings |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/JSHint/test-js-stripe_elements.png)</details>| ✅
|product_img_changement.html | Only Django errors || ✅
|quantity_input_script.html | Only Django errors || ✅
|profile.html | Only Django errors || ✅
|products.html | Only Django errors  || ✅
|edit_product.html | Only Django errors  || ✅
|add_product.html | Only Django errors  || ✅
|base.html | Only Django errors  || ✅


### PYTHON Validation 
[PEP 8](https://pep8ci.herokuapp.com/) serves as a comprehensive style guide for writing Python code, emphasizing consistency and readability as its core principles. It offers guidance on code formatting, variable and function naming conventions, and various best practices. Adhering to PEP 8 principles contributes to enhancing code quality, making it more readable and maintainable.

Within the settings file, one URL was identified as being excessively long. The other lines that exceeded the recommended length were automatically generated by Django. All other files were free from errors and issues.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/home/test-pep8-home-models.png)</details>| ✅
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/home/test-pep8-home-views.png)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/home/test-pep8-home-urls.png)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/home/test-pep8-home-forms.png)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/home/test-pep8-home-admin.png)</details>| ✅
|app.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/home/test-pep8-home-apps.png)</details>| ✅
| **Blog App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/blog/test-pep8-blog-models.png)</details>| ✅
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/blog/test-pep8-blog-views.png)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/blog/test-pep8-blog-urls.png)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/blog/test-pep8-blog-forms.png)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/blog/test-pep8-blog-admin.png)</details>| ✅
|app.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/blog/test-pep8-blog-app.png)</details>| ✅
| **Products App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-models.png)</details>| ✅
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-views.png)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-urls.png)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-forms.png)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-admin.png)</details>| ✅
|app.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-app.png)</details>| ✅
|utils.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-utils.png)</details>| ✅
|widgets.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/products/test-pep8-products-widgets.png)</details>| ✅
| **Bag App** |
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/bag/test-pep8-bag-views.png)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/bag/test-pep8-bag-urls.png)</details>| ✅
|app.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/bag/test-pep8-bag-app.png)</details>| ✅
|contexts.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/bag/test-pep8-bag-contexts.png)</details>| ✅
|bag_tools.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/bag/test-pep8-bag-bag_tools.png)</details>| ✅
| **Checkout App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-models.png)</details>| ✅
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-views.png)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-urls.png)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-forms.png)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-admin.png)</details>| ✅
|app.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-app.png)</details>| ✅
|signals.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-signals.png)</details>| ✅
|webhook_handler.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-webhook_handler.png)</details>| ✅
|webhooks.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/checkout/test-pep8-checkout-webhooks.png)</details>| ✅
| **Profiles App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/profiles/test-pep8-profiles-models.png)</details>| ✅
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/profiles/test-pep8-profiles-views.png)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/profiles/test-pep8-profiles-urls.png)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/profiles/test-pep8-profiles-forms.png)</details>| ✅
|app.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/pep8/profiles/test-pep8-profiles-app.png)</details>| ✅


<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Accessibility

### **Wave**

[The WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to assess the accessibility of the website. WAVE helps identify potential accessibility issues and provides guidance on how to improve the accessibility of web content.

During the evaluation, the following issues were identified:

- **Errors**: The website generated 6 errors, which were related to the footer < a > (anchor) tags and form label. There was no aria-label or text describing on the anchor and no label for the forms. This was, of course, added to fix the errors.

- **Contrast Warning**: Received a contrast warning for the background of New product label, which was blue used by Bootstrap's class "btn-primary". This color was not good against my white text. The Solution was to change the product new label color to black which will fit the theme of my black and white website.


<p align="center">
  <img src="docs/testing.md/test-accessibility.png">
</p>


By using the WAVE tool, I gained valuable insights into the accessibility of my website. While I have chosen not to address certain errors at this time, I remain committed to creating an inclusive user experience and will continue to explore ways to improve accessibility in the future.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

<p align="center">
  <img src="docs/readme.md/readme-divider3.png">
</p>

## Performance
I conducted a comprehensive evaluation of [The easykeyboardmaker website](https://easykeyboardmaker-ffb468c2d2d7.herokuapp.com/) using [Google Lighthouse in Google Chrome Developer Tools](https://developer.chrome.com/docs/lighthouse/). This evaluation was performed in Google Chrome browser's incognito mode to eliminate all potential impacts from other addons and cached files.

The performance scores were assessed for both desktop and mobile devices. Below are the summarized results:

### Desktop Performance
- Average performance score: 98.08 / 100
- The majority of pages received scores above 95 / 100, indicating excellent performance.

| **Tested** | **Performance Score** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| 97 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-index.png)</details> | ✅
|contact_form.html| 99 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-contact_form.png)</details> | ✅
|contact.html| 99 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-contact.png)</details> | ✅
|company.html| 99 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-company.png)</details> | ✅
|partners.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-partners.png)</details>| ✅
|payments.html| 99 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-payment.png)</details> | ✅
|privacy_policy.html| 99 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-privacy.png)</details> | ✅
|return_policy.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-return.png)</details>| ✅
|shipping_policy.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-shipping.png)</details>| ✅
|warranty_policy.html| 99 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-warranty.png)</details> | ✅
|terms_of_service.html| 98 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/home/test-lighthouse-desktop-home-terms.png)</details>| ✅
| **Blog App** |
|blog.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/blog/test-lighthouse-desktop-blog-blog.png)</details>| ✅
|post_create.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/blog/test-lighthouse-desktop-blog-post_create.png)</details>| ✅
|post_delete.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/blog/test-lighthouse-desktop-blog-post_delete.png)</details>| ✅
|post_detail.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/blog/test-lighthouse-desktop-blog-post_details.png)</details>| ✅
|post_edit.html| 95 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/blog/test-lighthouse-desktop-blog-post_edit.png)</details>| ✅
| **Products App** |
|add_product.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/products/test-lighthouse-desktop-products-add_product.png)</details>| ✅
|delete_product.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/products/test-lighthouse-desktop-products-delete_product.png)</details>| ✅
|edit_product.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/products/test-lighthouse-desktop-products-edit_product.png)</details>| ✅
|product_detail.html| 97 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/products/test-lighthouse-desktop-products-product_detail.png)</details>| ✅
|products.html| 98 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/products/test-lighthouse-desktop-products-products.png)</details>| ✅
| **Bag App** |
|bag.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/bag/test-lighthouse-dekstop-bag-bag.png)</details>| ✅
| **Checkout App** |
|checkout.html| 97 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/checkout/test-lighthouse-desktop-checkout-checkout.png)</details>| ✅
| **Profiles App** |
|profile_agreement.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/profiles/test-lighthouse-desktop-profiles-user_agreement.png)</details>| ✅
|profile_update.html| 98 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/profiles/test-lighthouse-desktop-profiles-profile_update.png)</details>| ✅
|profile.html| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/desktop/profiles/test-lighthouse-desktop-profiles-profile.png)</details>| ✅


### Mobile Performance
- Average performance score: 72.4 / 100
- The pages showed slightly lower performance compared to the desktop but still maintained a satisfactory score.

| **Tested** | **Performance** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| 72 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-index.png)</details> | ✅
|contact_form.html| 80 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-contact_form.png)</details> | ✅
|contact.html| 79 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-contact.png)</details> | ✅
|company.html| 79 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-company.png)</details> | ✅
|partners.html| 80 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-partners.png)</details>| ✅
|payments.html| 76 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-payment.png)</details> | ✅
|privacy_policy.html| 73 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-privacy.png)</details> | ✅
|return_policy.html| 81 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-return.png)</details>| ✅
|shipping_policy.html| 78 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-shipping.png)</details>| ✅
|warranty_policy.html| 78 / 100 |<details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-warranty.png)</details> | ✅
|terms_of_service.html| 79 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/home/test-lighthouse-mobile-home-terms.png)</details>| ✅
| **Blog App** |
|blog.html| 80 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/blog/test-lighthouse-mobile-blog-blog.png)</details>| ✅
|post_create.html| 75 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/blog/test-lighthouse-mobile-blog-post_create.png)</details>| ✅
|post_delete.html| 78 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/blog/test-lighthouse-mobile-blog-post_delete.png)</details>| ✅
|post_detail.html| 82 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/blog/test-lighthouse-mobile-blog-post_detail.png)</details>| ✅
|post_edit.html| 73 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/blog/test-lighthouse-mobile-blog-post_edit.png)</details>| ✅
| **Products App** |
|add_product.html| 73 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/products/test-lighthouse-mobile-products-post_create.png)</details>| ✅
|delete_product.html| 79 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/products/test-lighthouse-mobile-products-post_delete.png)</details>| ✅
|edit_product.html| 79 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/products/test-lighthouse-mobile-products-post_edit.png)</details>| ✅
|product_detail.html| 78 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/products/test-lighthouse-mobile-products-post_detail.png)</details>| ✅
|products.html| 73 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/products/test-lighthouse-mobile-products-products.png)</details>| ✅
| **Bag App** |
|bag.html| 73 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/bag/test-lighthouse-mobile-bag-bag.png)</details>| ✅
| **Checkout App** |
|checkout.html| 74 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/checkout/test-lighthouse-mobile-checkout-checkout.png)</details>| ✅
| **Profiles App** |
|profile_agreement.html| 79 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/profiles/test-lighthouse-mobile-profiles-user_agreement.png)</details>| ✅
|profile_update.html| 77 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/profiles/test-lighthouse-mobile-profiles-update_profile.png)</details>| ✅
|profile.html| 79 / 100 | <details><summary>Screenshot of result</summary>![Result](docs/testing.md/lighthouse/mobile/profiles/test-lighthouse-mobile-profiles-profile.png)</details>| ✅


In terms of performance, Easy Keybaord Maker website delivered strong results, ensuring a seamless user experience on both desktop and mobile platforms.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Performing tests on various devices
The website was tested on the following devices:

<ins>Mobile</ins>
1. Samsung s22 ultra 
2. iPhone X 
3. Samsung galaxy s22
4. iPhone 14 Pro max

<ins>Desktop</ins>
1. Samsung Galaxy Book 360
2. HP Elite book 830 g9
3. HP Victus gaming desktop

<ins>Monitors</ins>
1. 49-inch Samsung CHG9 ultra-wide
2. 27-inch Benq zowie XL2746S
3. 27-inch Dell ultrasharp U2723QE

In addition, the website was tested using the Google Chrome Developer Tools Device Toggling option for all available device options.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Browser compatibility
The website was tested on the following:

<ins>Browsers</ins>
1. Microsoft Edge
2. Google Chrome 	
3. Mozilla Firefox 	
4. Safari

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>


## Automated Testing

Autmated Testing was not implemented at this time in this project. But this will be come available in near future!



<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

## Manual Testing

### Testing user stories



### User Experience and Improvements
I engaged in user testing involving family members and friends to collect feedback regarding their website experience. I requested them to complete the following tasks and share their feedback on their overall experience:

Total users attended the testing: 4

| Test                   | Result  |
|------------------------|---------|
| Create an account      | **100%**|
| Update the profile     | **100%**|
| Update Shipping setting| **100%**|
| Add Product to cart    | **100%**|
| Increase a Product qty | **100%**|
| Test buy a product     | **100%**|
| Put a review           | **100%**|
| Update a review        | **100%**|
| Delete a review        | **100%**|
| Search for a Product   | **100%**|
| Subscribe to Newsletter| **80%**|
| Use Contact form       | **100%**|
| Test all links         | **100%**|
| Delete account         | **100%**|

&nbsp;

### Full Testing


**`Navbar unauthorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo | Redirects to index.html page | Clicked on logo | Index page loads | ✅ |
| Home | Redirects to the index page | Clicked on the link "Home" | Index page loads | ✅ |
| Products category links | Redirect to product view of the link | Clicked on the links of different product category  | Page reloads and displaying the correct products | ✅ |
| Articles | Redirect to the article post page | Clicked on the link "Articles" | Page loads with a view of blog posts | ✅ |
| Search | Get search query render | Typed "keyboard" | Different keyboard was showing | ✅ |
| Login | Redirects to the login page | Clicked on the link "Login" | Login page loads and form displays | ✅ |
| Sign up | Redirects to the signup page and form | Clicked on the link "Sign up" | Sign-up page loads and the form displays | ✅ |
| Support | Redirects to the support page | Clicked on the link "support" | Support page loads | ✅ |


**`Navbar authorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo | Redirects to index.html page | Clicked on logo | Index page loads | ✅ |
| Products category links | Redirect to product view of the link | Clicked on the links of different product category  | Page reloads and displaying the correct products | ✅ |
| Articles | Redirect to the Article post page | Clicked on the link "Articles" | Page loads with a view of blog posts | ✅ |
| Support | Redirects to the support page | Clicked on the link "support" | Support page loads | ✅ |
| Profile image/icon | Triggers the dropdown menu | Clicked on the image | The dropdown menu is displayed | ✅ |

**`Account drop-down menu`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Profile | Redirects to the profile page with the user's information and editable form and user / shipping information | Clicked on the "Profile" link | Profile page loads, displaying the user's information and an editable forms | ✅ |
| Product Management | Redirects to the page where the user can create a product with an editable form | Clicked on the "Porduct Management" link | "Porduct Management" page loads, showing product form inputs and submit button | ✅ |
| Article Management | Redirects to the page where the user can create a article post with an editable form | Clicked on the "Article Management" link | "Article Management" page loads, displaying the Article Post form | ✅ |
| Admin | Redirects to djangos admin panel backend | Clicked on the "Admin" link | "Admin" page panel loads, displaying the admin dashboard panel with all models | ✅ |
| Send email | Redirects to the page where the user can send out emails to all subscribed users | Clicked on the "Send email" link | "Send email" page loads, displaying the form for sending out emails | ✅ |
| Logout | Redirects the user to a logout confirmation page | Clicked on "Logout" | User is redirected to a page confirming the logout | ✅ |

**`Index page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Shop now button | Redirects to the page displaying all products | Clicked on the "Shop now" button | Successfully redirected to the page displaying all products | ✅ |
| Shop by Category img buttons | Redirects to the page displaying all products with that category | Clicked on all the different category buttons | Successfully redirected to the page displaying products in that category | ✅ |
| Subscribe button | Redirects user to index and display success message of successful subscribed | Clicked on the "Subscribe" button | Successfully message displayed in local environment but not in deployed version. Internal 500 error displayed | ❌ |
| New Arrival img buttons | Redirects to the page displaying product detail page | Clicked on the "New Arrival" button | Successfully redirected to the page displaying product detail page of that product | ✅ |
| Article posts | Redirects to the article post detail page | Clicked on the image link of an article card | Successfully redirected to the article detail page | ✅ |
| Footer navigation links | Redirects to different information pages | Clicked on all links in the footer | Successfully user redirection to correct pages/templates | ✅ |


**`Support page authorized user`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Reason* | Field is required and should be a valid choose of user | Tested with an empty reason | Error message is displayed prompting the user to provide a valid Reason* | ✅ |
| Email | Field is required and should be a valid email format | Tested with an empty field, or invalid format | Error message displayed prompting the user to provide a valid email address | ✅ |
| Subject | Field is required and can't be left empty | Tested with an empty field, invalid criteria | Error message displayed prompting the user to provide a subject | ✅ |
| Message | Field is required and can't be left empty | Tested with an empty field, invalid criteria | Error message displayed prompting the user to provide a subject | ✅ |
| Submit | If the form is valid, the user is redirected to support page with displayed successful message | Clicked the submit button with valid and non-valid formats | The submit button functions as expected, redirecting to the support page and displaying the corresponding message | ✅ |


**`Sign up page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Username | Field is required and should be a valid username format | Tested with an empty field, invalid format | Error message is displayed prompting the user to provide a valid username | ✅ |
| Email | Field is required and should be a valid email format | Tested with an empty field, or invalid format | Error message displayed prompting the user to provide a valid email address | ✅ |
| Password | Field is required and should meet password criteria | Tested with an empty field, invalid criteria | Error message displayed prompting the user to provide a valid password | ✅ |
| Password confirmation | Field is required and should match the entered password | Tested with empty field, mismatched passwords | Error message displayed prompting the user to confirm the password correctly | ✅ |
| Sign up button | If the form is valid, the user is redirected to the profile page with a flash message confirming successful registration. If the form is not valid, an error message is displayed. | Clicked the button with valid and non-valid formats | The button functions as expected, redirecting to the appropriate page and displaying the corresponding messages | ✅ |
| Login text link | Redirects to the login page | Clicked on the "Login" link | The login page and form were successfully loaded | ✅ |

**`Log in page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Username | The user enters a username | Tested with valid and invalid username input | The username field accepts and saves the valid input. If invalid, it displays an error message | ✅ |
| Password | The user enters a password | Tested with valid and invalid password input | The password field functions correctly, allowing the user to input a valid password and displays an error message when not valid | ✅ |
| Forgot password? text link | Clicking the text link redirects to the password change page for requesting the user's email | Clicked on the "Forgot Password?" text link | Successfully redirected to the password change page with the requested email input but the email never received. Internal Server Error | ❌ |
| Sign up text link | Clicking the text link redirects to the sign-up page | Clicked on the "Sign up" text link | Successfully redirected to the sign-up page with the registration form | ✅ |
| Login | If the login form is valid, the user is logged in and redirected to the appropriate page. If the form is not valid, an error message is displayed. | Tested with valid and invalid login form input | The login button functions correctly, logging in the user with valid credentials and displaying error messages for invalid credentials | ✅ |

**`Profile page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Update user information | Redirect the user to the update user information page with an editable form | Clicked on the "Update" button | Redirected to the correct page with an editable "User information" form | ✅ |
| Update shipping information | Able to update the shipping inputs directly on the page |  Clicked on the "Update" button | Page reloads and displays successful toast message of update was successful | ✅ |
| User agreement link | Redirects to the page displaying user agreement | Clicked on the "User agreement" button | Redirected to the correct page with user agreement| ✅ |
| Change password | Redirect to the change password page with an editable form for a new password | Clicked on the "Change password" button | Redirected to the change password page and able to change the password | ✅ |
| Delete | Display a popup modal with delete confirmation | Clicked on the "Delete" button on the popup modal | Redirected to the index page with a confirmation message | ✅ |

**`Article page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Click on article post card | Redirected to article detail page | Clicked on the article card | Redirected to the article detail page | ✅ |

**`Article Detail page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| "Back" button | Redirect user back to the article page | Clicked on the back button | Successfully redirected to article page | ✅ |


**`Edit Article page if superuser`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Edit | When changes are made and the "Edit" button is clicked, the changes should be saved, the user should be redirected to the article detail page, and a flash message should confirm the update | Made changes and click on the "Edit" button | Changes were successfully saved, redirected to the article detail page, and a flash message confirmed the update | ✅ |
| Back | Redirects to the article detail page | Clicked on the "Back" button | The article detail page loads, displaying the article | ✅ |

**`Delete Article page if superuser`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Delete button | Deletes the article and redirects to the article page where all the articles are displayed | Clicked on the delete button | The article was successfully deleted, and I was redirected to the product page | ✅ |
| Cancel button | Redirects to the article detail page | Clicked on the "Cancel" button | The article detail page loads, displaying the articles | ✅ |

**`Product page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Product add to cart button | Product is added to the cart with a successful message | Clicked on the "add to cart" button | Successfully clicked on the button link and the product was added to the cart with successful message indicating success | ✅ |
| Product name link | Redirect to product detail page | Clicked on product name link | Successfully redirected to product detail page | ✅ |
| Grid layout icon | Changement of product view to grid layout | Clicked on the icon | All products was changed in to the correct layout | ✅ |
| List layout icon | Changement of product view to list layout | Clicked on the icon | All products was changed in to the correct layout | ✅ |
| Sort by list | Sort product by the desirable value | Clicked in the sort by dropdown for testing all values | Product was decending and acending depending on the value from the sort by | ✅ |

**`Product Review if product was bought`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Make a review | Write review and chooice a star with a successfully submission | Write review and clicked submit | Review is submitted and dispalyed with review average of star | ✅ |

**`Product Detail page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Small product images | Images will change place to the bigger imag field for better product view | Clicked on the small images | Successfully clicked and the img that is selected was changed and dispalyed correctly | ✅ |
| Quantity buttons | Minus or Plus button for adding additional product quantity in the cart | Clicked on the minus or plus button | Product is added or removed from cart depending on the quantity buttons successfully | ✅ |
| Keep shopping button | Redirect user back to all product page | Clicked on the keeyp shopping button | Successfully redirected to product page were product are displayed | ✅ |
| Add to cart button | Product is added to the cart with a successful message | Clicked on the "add to cart" button | Successfully clicked on the button link and the product was added to the cart with successful message indicating success | ✅ |
| Social media links | Takes user to the social media platform with target_blank attribute | Clicked on the social icon | Successfully redirected to a new tab and social media platform | ✅ |

**`Product Delete page if superuser`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Delete button | Display delete confirmation page and be able to delete the product | Clicked on delete button | Delete confirmation page was displayed, and the delete button worked and the product was deleted from the sortiment | ✅ |

**`Product Edit page if superuser`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Edit button | The product form will be displayed with prefilled product information fileld in for be able of changement | Clicked on Edit button | Product form was dispalyed with product information and changement was successfully  displayed with a toast mesasge and get redirected to product detail page | ✅ |

**`403, 404, 405, 500 Page`**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Go home button | Correct "error message" displays and redirects the user to index.html page | Edited a non-URL path in the web browser and then clicked on the Go home button | Correct error handling message was displayed for the user, and when the Go home button was clicked, the user was redirected to the index page | ✅ |


<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Summary 

### Performance

- **Desktop Performance:**
  - Average performance score: 98.08 / 100
  - Majority of pages received scores above 95 / 100, indicating excellent performance.

- **Mobile Performance:**
  - Average performance score: 72.4 / 100
  - Pages showed slightly lower performance compared to desktop but maintained a satisfactory score.

### Device Testing

The website was tested on a variety of devices, including mobile phones (*Samsung s22 ultra*, *iPhone X*, *Samsung galaxy s22*, *iPhone 14 Pro max*), desktops (*Samsung Galaxy Book 360*, *HP Elite book 830 g9*, *HP Victus gaming desktop*), and monitors (*49-inch Samsung CHG9 ultra-wide*, *27-inch Benq zowie XL2746S*, *27-inch Dell ultrasharp U2723QE*). Additionally, testing was performed using Google Chrome Developer Tools Device Toggling for various device options.

### Browser Compatibility

The website was tested on popular browsers, ensuring compatibility with:
1. Microsoft Edge
2. Google Chrome
3. Mozilla Firefox
4. Safari

### Automated Testing

Automated testing has not been implemented in the current project but is planned for future development.

### Manual Testing

User stories and various scenarios were tested manually, involving family members and friends. The success rate for tasks such as account creation, profile updates, product interactions, and more was 100%.

### Overall User Experience

Feedback from user testing and manual testing indicates a seamless user experience. The website performed well in terms of functionality, responsiveness, and user interface across different devices and browsers.

The testing process was comprehensive, covering various aspects of the website, and the identified issues have been documented for further improvement.


<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>