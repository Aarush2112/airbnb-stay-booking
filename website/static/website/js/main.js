document.addEventListener('DOMContentLoaded', function () {
  // Mobile navigation toggle
  const header = document.querySelector('.site-header');
  const toggleBtn = document.querySelector('.nav-toggle');
  if (header && toggleBtn) {
    toggleBtn.addEventListener('click', function () {
      const expanded = header.classList.toggle('nav-open');
      toggleBtn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    });
  }

  // Live nightly price estimator on stay detail page
  const checkInInput = document.getElementById('id_check_in');
  const checkOutInput = document.getElementById('id_check_out');
  const estimateBox = document.getElementById('price-estimate');

  if (checkInInput && checkOutInput && estimateBox) {
    const rate = parseFloat(estimateBox.dataset.rate || '0');
    const updateEstimate = function () {
      if (!checkInInput.value || !checkOutInput.value || !rate) {
        estimateBox.style.display = 'none';
        return;
      }
      const start = new Date(checkInInput.value);
      const end = new Date(checkOutInput.value);
      const diffDays = Math.round((end - start) / (1000 * 60 * 60 * 24));
      if (diffDays > 0) {
        estimateBox.textContent = `${diffDays} night(s) × $${rate} = $${diffDays * rate} estimated total`;
        estimateBox.style.display = 'block';
      } else {
        estimateBox.style.display = 'none';
      }
    };

    checkInInput.addEventListener('change', updateEstimate);
    checkOutInput.addEventListener('change', updateEstimate);
  }
});
