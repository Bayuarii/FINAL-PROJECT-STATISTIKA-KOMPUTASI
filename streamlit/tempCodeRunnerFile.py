<style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f7fa;
    }
    .main-title {
        text-align: center;
        color: #3d85c6;
        animation: fadeIn 2s;
    }
    .sub-title {
        text-align: center;
        color: #6aa84f;
        margin-bottom: 20px;
        animation: fadeInUp 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    .card {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
        padding: 20px;
        margin: 10px 0;
        animation: fadeIn 2s;
    }
    .dataframe {
        text-align: center;
        color: #333;
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 10px;
        font-size: 14px;
    }
    .dataframe th, .dataframe td {
        text-align: center; /* Menambahkan untuk memusatkan semua teks */
        padding: 8px;
    }
    .dataframe th {
        background-color: #3d85c6;
        color: #fff;
    }
</style>