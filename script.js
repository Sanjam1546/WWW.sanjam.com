function submitVote() {
    const options = document.getElementsByName('vote');
    let selectedOption = null;
    for (const option of options) {
        if (option.checked) {
            selectedOption = option.value;
            break;
        }
    }

    if (selectedOption) {
        alert(`You voted for ${selectedOption}`);
        // Here you can add the logic to update the results
    } else {
        alert('Please select an option to vote');
    }
}
