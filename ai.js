const axios = require('axios');

// URL của website bạn muốn gửi yêu cầu
const url = 'https://l7.count123.org/test.php';

axios.get(url)
    .then(response => {
        console.log('Yêu cầu thành công!');
        console.log('Mã trạng thái:', response.status);
        console.log('Nội dung:', response.data);
    })
    .catch(error => {
        if (error.response) {
            console.log('Yêu cầu không thành công, mã trạng thái:', error.response.status);
        } else {
            console.log('Có lỗi xảy ra:', error.message);
        }
    });
    