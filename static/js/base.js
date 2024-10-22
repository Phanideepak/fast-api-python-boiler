    // Add Department JS
    const departmentForm = document.getElementById('departmentForm');
    if (departmentForm) {
        departmentForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const form = event.target;
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            const payload = {
                name: data.name,
                description: data.description,
            };

            try {
                const response = await fetch('/dept', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${getCookie('access_token')}`
                    },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {
                    form.reset(); // Clear the form
                    window.location.href = '/dept/department-page';
                } else {
                    // Handle error
                    const errorData = await response.json();
                    alert(`Error: ${errorData.exception}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }

    // Edit Department JS
    const editDepartmentForm = document.getElementById('editDepartmentForm');
    if (editDepartmentForm) {
        editDepartmentForm.addEventListener('submit', async function (event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        var url = window.location.pathname;
        const id = url.substring(url.lastIndexOf('/') + 1);

        const payload = {
            id : id,
            name: data.name,
            description: data.description,
        };

        try {
            const token = getCookie('access_token');
            if (!token) {
                throw new Error('Authentication token not found');
            }

            const response = await fetch(`/dept`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(payload)
            });

            if (response.ok) {
                window.location.href = '/dept/department-page';
            } else {
                // Handle error
                const errorData = await response.json();
                alert(`Error: ${errorData.exception}`);
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        }
    });
     
    }

    const deleteDepartmentButton = document.getElementById('deleteDepartmentButton');

    if(deleteDepartmentButton){
        //Delete Department JS
        document.getElementById('deleteDepartmentButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);

            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/dept?id=${id}`, {
                    method: 'DELETE',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/dept/department-page';
                } else {
                    // Handle error
                    const errorData = await response.json();
                    alert(`Error: ${errorData.exception}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }

    const approveDepartmentButton = document.getElementById('approveDepartmentButton')

    if(approveDepartmentButton){
        //Approve Department JS
        document.getElementById('approveDepartmentButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);
            
            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/dept/approve?id=${id}`, {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/dept/department-page';
                } else {
                    // Handle error
                    const errorData = await response.json();
                    alert(`Error: ${errorData.exception}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }

    const restoreDepartmentButton = document.getElementById('restoreDepartmentButton')

    if(restoreDepartmentButton){
        //Restore Department JS
        document.getElementById('restoreDepartmentButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);

            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/dept/restore?id=${id}`, {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/dept/department-page';
                } else {
                    // Handle error
                    const errorData = await response.json();
                    alert(`Error: ${errorData.exception}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }



    // Login JS
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const form = event.target;
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            

            const payload = {
                email: data.email,
                password: data.password,
            };
            
            try {
                const response = await fetch('/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {
                    // Handle success (e.g., redirect to dashboard)
                    const data = await response.json();
            
                    // Delete any cookies available
                    logout();
                    // Save token to cookie
                    document.cookie = `access_token=${data.data.access_token}; path=/`;
                    
                    window.location.href = '/dept/department-page'; // Change this to your desired redirect page
                } else {
                    // Handle error
                    const errorData = await response.json();
                    alert(`Error: ${errorData.exception}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }

    // Register JS
    const registerForm = document.getElementById('registerForm');
    
    if (registerForm) {

        registerForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const form = event.target;
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            const payload = {
                email: data.email,
                firstname: data.firstname,
                lastname: data.lastname,
                password: data.password,
                confirm_password : data.confirm_password
            };
            
            
            
            try {
                const response = await fetch('/auth/signup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                if (response.ok) {
                    window.location.href = '/auth/login-page';
                } else {
                    // Handle error
                    const errorData = await response.json();
                    alert(`Error: ${errorData.exception}`);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
        });
    }





    // Helper function to get a cookie by name
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    function logout() {
        // Get all cookies
        const cookies = document.cookie.split(";");
    
        // Iterate through all cookies and delete each one
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i];
            const eqPos = cookie.indexOf("=");
            const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
            // Set the cookie's expiry date to a past date to delete it
            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
        }
    
        // Redirect to the login page
        window.location.href = '/auth/login-page';
    };