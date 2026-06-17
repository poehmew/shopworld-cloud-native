import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyB54yypPxnUelwU9avwpYtVjhatc6aG2kY",
  authDomain: "shopworld-demo.firebaseapp.com",
  projectId: "shopworld-demo",
  storageBucket: "shopworld-demo.firebasestorage.app",
  messagingSenderId: "37435775554",
  appId: "1:37435775554:web:a37994751770cb8e54abdb",
  measurementId: "G-ZKY7ZPGLX3"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();
