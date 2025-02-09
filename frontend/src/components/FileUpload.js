import { useState } from "react";
import axios from "axios";
import { Button, CircularProgress } from "@mui/material";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!file) return;
    setUploading(true);
    
    const formData = new FormData();
    formData.append("file", file);
    
    try {
      const response = await axios.post("http://localhost:8000/documents/upload/", formData);
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Error uploading file.");
    }

    setUploading(false);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <Button variant="contained" onClick={handleUpload} disabled={uploading}>
        {uploading ? <CircularProgress size={20} /> : "Upload"}
      </Button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default FileUpload;
