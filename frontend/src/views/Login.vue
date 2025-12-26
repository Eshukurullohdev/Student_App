<template>
  <div class="login">
    <h2>Login</h2>

    <form @submit.prevent="login">
      <input
        v-model="email"
        type="email"
        placeholder="Email"
        required
      />

      <input
        v-model="password"
        type="password"
        placeholder="Password"
        required
      />

      <button type="submit">Login</button>
    </form>

    <p v-if="error" style="color:red">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "../services/api";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const error = ref("");
const router = useRouter();

const login = async () => {
  try {
    const response = await api.post("/auth/login/", {
      email: email.value,
      password: password.value,
    });

    // TOKEN SAQLAYMIZ
    localStorage.setItem("access", response.data.access);
    localStorage.setItem("refresh", response.data.refresh);

    // PROFILGA O‘TAMIZ
    router.push("/profile");
  } catch (err) {
    error.value = "Login yoki parol noto‘g‘ri";
  }
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 50px auto;
}
input {
  display: block;
  width: 100%;
  margin-bottom: 10px;
  padding: 8px;
}
button {
  width: 100%;
  padding: 10px;
}
</style>
