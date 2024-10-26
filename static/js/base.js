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

    const addEmployeeForm = document.getElementById('addEmployeeForm');
    if (addEmployeeForm) {
        addEmployeeForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const form = event.target;
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            const payload = {
                firstname: data.firstname,
                lastname: data.lastname,
                contact : data.contact,
                designation : data.designation,
                eid : data.eid,
                dept_id : data.dept_id
            };


            try {
                const response = await fetch('/emp', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${getCookie('access_token')}`
                    },
                    body: JSON.stringify(payload)
                });
                
                if (response.ok) {
                    form.reset(); // Clear the form
                    window.location.href = '/emp/employee-page';
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

    // Add Address JS
    const addAddressForm = document.getElementById('addAddressForm');
    if (addAddressForm) {
        addAddressForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const form = event.target;
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            const payload = {
                first_line : data.first_line,
                second_line : data.second_line,
                land_mark : data.landmark,
                phone : data.phone,
                city: data.city,
                pincode: data.pincode,
                state : data.state
            };


            try {
                const response = await fetch('/address', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${getCookie('access_token')}`
                    },
                    body: JSON.stringify(payload)
                });
                
                if (response.ok) {
                    form.reset(); // Clear the form
                    window.location.href = '/address/address-page';
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

    const editAddressForm = document.getElementById('editAddressForm');
    if (editAddressForm) {
        editAddressForm.addEventListener('submit', async function (event) {
            event.preventDefault();

            const form = event.target;
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);

            const payload = {
                id : id,
                first_line : data.first_line,
                second_line : data.second_line,
                land_mark : data.landmark,
                phone : data.phone,
                city: data.city,
                pincode: data.pincode,
                state : data.state
            };


            try {
                const response = await fetch('/address', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${getCookie('access_token')}`
                    },
                    body: JSON.stringify(payload)
                });
                
                if (response.ok) {
                    form.reset(); // Clear the form
                    window.location.href = '/address/address-page';
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

    const editEmployeeForm = document.getElementById('editEmployeeForm');
    if (editEmployeeForm) {
        editEmployeeForm.addEventListener('submit', async function (event) {
            event.preventDefault();
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);
            const form = event.target;
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());

            const payload = {
                firstname: data.firstname,
                lastname: data.lastname,
                contact : data.contact,
                designation : data.designation,
                eid : data.eid,
                dept_id : data.dept_id
            };


            try {
                const response = await fetch('/emp', {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${getCookie('access_token')}`
                    },
                    body: JSON.stringify(payload)
                });
                
                if (response.ok) {
                    form.reset(); // Clear the form
                    window.location.href = '/emp/employee-page';
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

    const deleteAddressButton = document.getElementById('deleteAddressButton');

    if(deleteAddressButton){
        //Delete Address JS
        document.getElementById('deleteAddressButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);

            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/address?id=${id}`, {
                    method: 'DELETE',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/address/address-page';
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

    const makeAddressPrimaryButton = document.getElementById('makeAddressPrimaryButton')

    if(makeAddressPrimaryButton){
        //Restore Department JS
        document.getElementById('makeAddressPrimaryButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);

            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/address/primary?id=${id}`, {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/address/address-page';
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

    const deleteEmployeeButton = document.getElementById('deleteEmployeeButton');

    if(deleteEmployeeButton){
        //Delete Department JS
        document.getElementById('deleteEmployeeButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);

            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/emp?id=${id}`, {
                    method: 'DELETE',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/emp/employee-page';
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

    const approveEmployeeButton = document.getElementById('approveEmployeeButton')

    if(approveEmployeeButton){
        //Approve Employee JS
        document.getElementById('approveEmployeeButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);
            
            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/emp/approve?id=${id}`, {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/emp/employee-page';
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

    const restoreEmployeeButton = document.getElementById('restoreEmployeeButton')

    if(restoreEmployeeButton){
        //Restore Employee JS
        document.getElementById('restoreEmployeeButton').addEventListener('click', async function () {
            var url = window.location.pathname;
            const id = url.substring(url.lastIndexOf('/') + 1);

            try {
                const token = getCookie('access_token');
                if (!token) {
                    throw new Error('Authentication token not found');
                }

                const response = await fetch(`/emp/restore?id=${id}`, {
                    method: 'PATCH',
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                if (response.ok) {
                    // Handle success
                    window.location.href = '/emp/employee-page';
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


    // View Admin Departnent
    const viewAdminDepartmentButton = document.getElementById('viewAdminDepartmentButton');
    if (viewAdminDepartmentButton) {
        viewAdminDepartmentButton.addEventListener('click', async function (event) {
            event.preventDefault();
            window.location.href = '/dept/department-page';
        });
    }

    // viewAdminEmployeeButton
    const viewAdminEmployeeButton = document.getElementById('viewAdminEmployeeButton');
    if (viewAdminEmployeeButton) {
        viewAdminEmployeeButton.addEventListener('click', async function (event) {
            event.preventDefault();
            window.location.href = '/emp/employee-page';
        });
    }

    // viewAdminAddressButton
    const viewAdminAddressButton = document.getElementById('viewAdminAddressButton');
    if (viewAdminAddressButton) {
        viewAdminAddressButton.addEventListener('click', async function (event) {
            event.preventDefault();
            window.location.href = '/address/address-page';
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
                    window.location.href = '/user/home'; // Change this to your desired redirect page
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