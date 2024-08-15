# rencrypt.pyi

from typing import Optional, Any

class CipherMeta:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    # Define any other methods and properties relevant to CipherMeta

class Cipher:
    cipher: Any
    cipher_meta: CipherMeta

    def __init__(self, cipher_meta: CipherMeta, key: Any) -> None: ...

    def seal_in_place(
        self,
        buf: Any,
        plaintext_len: int,
        block_index: Optional[int] = ...,
        aad: Optional[bytes] = ...,
        nonce: Optional[bytes] = ...
    ) -> int: ...

    def seal_in_place_from(
        self,
        plaintext: Any,
        buf: Any,
        block_index: Optional[int] = ...,
        aad: Optional[bytes] = ...,
        nonce: Optional[bytes] = ...
    ) -> int: ...
    
    @staticmethod
    def copy_slice(src: Any, buf: Any) -> None: ...

class RingAlgorithm:
    pass

class RustCryptoAlgorithm:
    pass

class SodiumoxideAlgorithm:
    pass

class OrionAlgorithm:
    pass

def copy_slice_internal(dst: bytearray, src: bytes) -> None:
    """
    Copy data from src to dst using internal copying.

    Args:
        dst: Destination bytearray.
        src: Source byte sequence.
    """
    ...

def copy_slice_concurrently(dst: bytearray, src: bytes, chunk_size: int) -> None:
    """
    Copy data from src to dst using concurrent copying with specified chunk size.

    Args:
        dst: Destination bytearray.
        src: Source byte sequence.
        chunk_size: The size of chunks to use for concurrent copying.
    """
    ...
def copy_slice(src: bytes, dst: bytearray) -> None:
    """
    Copy data from src to dst. Uses internal copying for smaller slices and concurrent copying for larger slices.
    
    Args:
        src: Source byte sequence.
        dst: Destination bytearray.
    """
    ...

def split_plaintext_tag_nonce_mut(
    data: bytearray, 
    plaintext_len: int, 
    tag_len: int, 
    nonce_len: int
) -> Tuple[bytearray, bytearray, bytearray]:
    """
    Split data into (plaintext, tag, nonce) in mutable form.
    
    Args:
        data: Input bytearray containing plaintext, tag, and nonce.
        plaintext_len: Length of the plaintext portion.
        tag_len: Length of the tag portion.
        nonce_len: Length of the nonce portion.

    Returns:
        A tuple containing mutable bytearrays for plaintext, tag, and nonce.
    """
    ...

def split_plaintext_and_tag_nonce_mut(
    data: bytearray, 
    plaintext_and_tag_and_nonce_len: int, 
    nonce_len: int
) -> Tuple[bytearray, bytearray]:
    """
    Split data into (plaintext_and_tag, nonce) in mutable form.
    
    Args:
        data: Input bytearray containing plaintext, tag, and nonce.
        plaintext_and_tag_and_nonce_len: Length of the combined plaintext and tag portion.
        nonce_len: Length of the nonce portion.

    Returns:
        A tuple containing mutable bytearrays for plaintext_and_tag and nonce.
    """
    ...

def as_array_mut(arr: Union[bytearray, np.ndarray]) -> bytearray:
    """
    Convert a Python bytearray or numpy array to a mutable bytearray.
    
    Args:
        arr: The input bytearray or numpy array.

    Returns:
        A mutable bytearray view of the input data.

    Raises:
        TypeError: If the input is not a bytearray or numpy array.
    """
    ...

def as_array(arr: Union[bytearray, bytes, np.ndarray]) -> bytes:
    """
    Convert a Python bytearray, bytes, or numpy array to a bytes view.
    
    Args:
        arr: The input bytearray, bytes, or numpy array.

    Returns:
        A bytes view of the input data.

    Raises:
        TypeError: If the input is not a bytearray, bytes, or numpy array.
    """
    ...