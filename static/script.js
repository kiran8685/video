function startVideoConference() {
    const domain = 'meet.jit.si';
    const options = {
        roomName: ' Todays Topic', // Replace with a unique room name
        width: "100%",
        height: "100%",
        parentNode: document.body,
    };

    const api = new JitsiMeetExternalAPI(domain, options);
}
