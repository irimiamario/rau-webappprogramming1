function signup() {
    console.log("Congratulations! You have successfully created an account");
    let s = 0;
    for (let i = 0; i <= 50; i++) {
        s += i;
    }
    console.log(`Sum of all numbers up to 50: ${s}`);
}

function cancel() {
    console.log("Warning! You are about to reset your inputs. Are you sure you want to continue?");
}