// YOUR CODE GOES HERE
// just to be on safe side
addEventListener('DOMContentLoaded', () => {
    const commentsEl = document.getElementById('comments')

    // object destructuring in function
    // cool stuff - just to wet your appetite
    // alternatively I could write one normal argument: data
    // and refer to its fields as for example data.author
    function showComment({author, post_date, description}) {
        commentsEl.innerHTML += `<hr>
        <p>${author} (${post_date}) - ${description}</p>`
    }

    async function submitComment(event) {
        // log event object for debug purpose
        console.log(event);
        // very important to prevent default
        // what would happened otherwise?
        event.preventDefault();
        // get target form from event
        // not very useful now, when we bind to one specific form
        // but imagine we have more forms on page and try to
        // get one handler for all of them
        const form = event.target;
        const formData = new FormData(form);
        try {
            // send appropriate request
            // long time can pass between calling fetch and getting response
            const response = await fetch(form.action, { method: 'post', body: formData });
            // parse response as json
            const data = await response.json();
            console.log(formData.get("description"));
            console.log(data);
            // display added comment at current page (without reloading)
            showComment(data.data);
        } catch (err) {
            // best error handling
            alert(`something went wrong during form upload ${err}`);
        }
    }
    
    // get access to form element
    const formEl = document.getElementById('commentForm');
    // bind our handler to submit event
    formEl.addEventListener('submit', submitComment);
});
// END OF YOUR CODE
