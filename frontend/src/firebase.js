import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
  apiKey: "PASTE_FROM_FIREBASE",
  authDomain: "PASTE_FROM_FIREBASE",
  projectId: "PASTE_FROM_FIREBASE",
  storageBucket: "PASTE_FROM_FIREBASE",
  messagingSenderId: "PASTE_FROM_FIREBASE",
  appId: "PASTE_FROM_FIREBASE"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();
