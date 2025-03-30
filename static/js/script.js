//confirmatio nbefore pressin close account button
document.querySelectorAll(".closeAccBtn").forEach( button => {
    button.addEventListener("click", function() {
        let url = this.getAttribute("data-url");
        Swal.fire({
                title: "Are you sure you wish to delete this financila account?",
                text: "You will be redirected to confirmation page",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, take me there!",
                cancelButtonText: "Cancel"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = url;
                }
        });


    });
});
