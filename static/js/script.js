/* global glowCookies */
$(document).ready(function() {
    // Success toat message
    $('.toast').toast('show');

    // Manage cookies
    glowCookies.start('en', {
        style: 3,
        analytics: 'G-FH87DE17XF',
        facebookPixel: '990955817632355',
        policyLink: 'https://link-to-policy.com',
        hideAfterClick: true,
        position: "left",
        bannerColor: "black",
        manageColor: "black",
        acceptBtnBackground: "black",
    });

    // Automatically close toast messages
    setTimeout(function () {
        let messages = document.getElementById("msg");
        messages.classList.remove("show");
        messages.classList.add("hide");
    }, 3000);
});
