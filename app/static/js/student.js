// Event listener untuk tombol submit
document.getElementById('submit-student').addEventListener('click', async () => {
    // Ambil data dari form
    const form = document.getElementById('student-form');
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => data[key] = value);

    // Kirim data ke server menggunakan Fetch API
    const response = await fetch('/add_student_route', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    // Tanggapan dari server
    if (response.ok) {
        alert('Student added successfully');
        // Tutup modal
        const modal = bootstrap.Modal.getInstance(document.getElementById('addStudentModal'));
        modal.hide();

        // Reload halaman untuk memperbarui data
        location.reload();
    } else {
        const errorData = await response.json();
        alert(`Failed to add student: ${errorData.message}`);
    }
});